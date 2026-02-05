# app.py
import os
import torch
import torch.nn as nn
from flask import Flask, request, render_template, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import torchaudio
from speechbrain.inference import EncoderClassifier

# Fix Hugging Face symlink issue on Windows
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

torchaudio.set_audio_backend("soundfile")  # use soundfile backend
UPLOAD_FOLDER = "uploads"
ALLOWED_EXT = {"wav", "mp3", "m4a", "flac", "ogg", "opus"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__, 
    static_folder="static",  # Update static folder path
    template_folder="."
)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ----- Define the classifier (must match training arch) -----
class DeepfakeDetector(nn.Module):
    def __init__(self, embedding_dim=192, num_classes=2):
        super(DeepfakeDetector, self).__init__()
        self.fc1 = nn.Linear(embedding_dim, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, num_classes)
        self.logsoft = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return self.logsoft(x)


# ----- Load pretrained ECAPA encoder -----
print("Loading ECAPA encoder (speechbrain/spkrec-ecapa-voxceleb)...")
ecapa = EncoderClassifier.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    run_opts={"local_strategy": "copy"}  # safe for Windows
)

# ----- Load your trained classifier -----
MODEL_PATH = "deepfake_detector.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

detector = DeepfakeDetector(embedding_dim=192, num_classes=2).to(device)

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Classifier weights not found: {MODEL_PATH}")

print(f"Loading classifier weights from {MODEL_PATH} ...")
state = torch.load(MODEL_PATH, map_location=device)

# Handle checkpoint formats
if isinstance(state, dict) and "state_dict" in state:
    state = state["state_dict"]

# Remove "module." prefix if present
new_state = {k.replace("module.", ""): v for k, v in state.items()}
detector.load_state_dict(new_state)
detector.eval()
print("Model loaded successfully.")


# ----- Helpers -----
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


def extract_embedding_from_file(path):
    """Extract embeddings from audio file using ECAPA encoder"""
    try:
        emb = ecapa.encode_file(path)  # returns (1, emb_dim)
        if isinstance(emb, torch.Tensor):
            emb = emb.squeeze(0)
            return emb.detach().to(device)
    except Exception as e:
        print("encode_file failed, fallback:", e)
        waveform, sr = torchaudio.load(path)
        if waveform.shape[0] > 1:  # stereo → mono
            waveform = waveform.mean(dim=0, keepdim=True)
        emb_batch = ecapa.encode_batch(waveform.to(device))
        emb = emb_batch.squeeze(0)
        return emb.detach().to(device)


# ----- Routes -----
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<page>")
def show_page(page):
    try:
        return render_template(page)
    except Exception as e:
        print(f"Error rendering {page}: {str(e)}")
        return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file part"}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        saved_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(saved_path)

        try:
            embedding = extract_embedding_from_file(saved_path)
            if embedding.dim() == 1:
                embedding = embedding.unsqueeze(0)
            embedding = embedding.to(device).float()

            with torch.no_grad():
                outputs = detector(embedding)
                probs = torch.exp(outputs).squeeze(0).cpu().numpy().tolist()
                class_idx = int(torch.argmax(outputs, dim=1).item())

                # ✅ Make sure this order matches training!
                labels = ["genuine", "synthetic"]
                predicted_label = labels[class_idx]
                confidence = float(probs[class_idx])

                # Debug print in terminal
                print(f"[DEBUG] File={filename}, class_idx={class_idx}, probs={probs}")

            return jsonify({
                "label": predicted_label,
                "confidence": confidence,
                "probs": probs,
                "filename": filename
            })

        except Exception as e:
            return jsonify({"error": f"Processing failed: {e}"}), 500

    return jsonify({"error": "Invalid file type"}), 400


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
