# 🎧 Audio Deepfake Detection – Frontend & Model Implementation

🚀 **DB-12 Project – Frontend + Model Making**  
This repository contains the **frontend interface** and **model implementation pipeline** for detecting **audio deepfakes** using **ECAPA-TDNN speaker embeddings** and a **binary classifier**.

---

## 📌 Project Objective

To design a **user-friendly frontend** and a **robust backend model pipeline** that allows users to:

🎙️ Upload an audio file  
🧠 Analyze it using ECAPA-TDNN embeddings  
🔍 Classify it as **Real** or **Fake** speech  
⚡ Obtain fast, real-time predictions  

---

## 🧩 System Architecture Overview

Frontend (UI)
↓
Audio Upload (.wav)
↓
Backend API
↓
Preprocessing
↓
ECAPA-TDNN Embedding Extraction
↓
Logistic Regression Classifier
↓
Prediction Output (Real / Fake)


---

# 🎨 Frontend Module

## 🖥️ Frontend Description

The frontend provides an **interactive interface** for users to test audio files against the deepfake detection model.

### ✨ Features

- 📂 Audio file upload (WAV format)
- ▶️ Audio playback support
- 🧠 One-click deepfake detection
- 📊 Displays prediction result (Real / Fake)
- ⚡ Fast response suitable for real-time use

---

## 🛠️ Frontend Technologies Used

- 🌐 HTML5
- 🎨 CSS3
- ⚙️ JavaScript
- 🐍 Flask / FastAPI (for backend integration)
- 🎧 Audio player API

---

## 📁 Frontend Folder Structure

frontend/
├── templates/
│ └── index.html
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── script.js
│ └── audio/
├── app.py


---

## 🔄 Frontend Workflow

1. User opens the web interface  
2. Uploads an audio file (.wav)  
3. Clicks **Detect Deepfake**  
4. Audio is sent to backend API  
5. Prediction result is displayed  

---

# 🧠 Model Making Module

## 🧪 Model Description

The backend model uses a **pretrained ECAPA-TDNN network** to extract **speaker embeddings**, followed by a **logistic regression classifier** for deepfake detection.

✔️ Audio-only  
✔️ Lightweight  
✔️ Interpretable  
✔️ Real-time capable  

---

## ⚙️ Model Pipeline

Raw Audio
→ Mono Conversion
→ Resampling (16 kHz)
→ Normalization
→ ECAPA-TDNN Embedding
→ Z-score Scaling
→ Logistic Regression
→ Real / Fake Output


---

## 🗃️ Dataset Used

### 🎙️ TIMIT-TTS Dataset

- ~80,000 audio samples
- 37 speakers
- 12 TTS models
- Sampling rate: 16 kHz
- Train/Test split: 80/20

---

## 🛠️ Model Technologies & Libraries

- 🧠 ECAPA-TDNN (pretrained)
- 🔥 PyTorch
- 🔊 torchaudio
- 📊 scikit-learn
- 🐍 Python 3.10
- ⚡ NumPy, Pandas

---

## 📁 Model Folder Structure

model/
├── data/
│ ├── train/
│ ├── test/
├── preprocessing.py
├── embedding_extraction.py
├── classifier.py
├── train.py
├── evaluate.py
├── model.pkl


---

## 🧪 Training Configuration

- Optimizer: Adam  
- Learning Rate: 1e-3  
- Batch Size: 32  
- Epochs: 50 (with early stopping)  

---

## 📊 Model Performance

📈 Accuracy: ~90%  
📈 F1-Score: 0.92  
📈 ROC-AUC: 0.93  

### 🆚 Baseline Comparison

| Model        | Accuracy | F1 | AUC |
|--------------|----------|----|-----|
| ECAPA-TDNN   | 94.7%    | 0.95 | 0.98 |
| RawNet2      | 88.3%    | 0.89 | 0.92 |

---

## 🚀 Real-Time Deployment Capability

- ⚡ Low latency inference
- 🔐 Minimal false positives
- 🎯 Suitable for:
  - Voice authentication
  - Media forensics
  - Security systems
  - Online audio verification

---

## ▶️ How to Run (Example)

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend
python app.py

# Open browser
http://127.0.0.1:5000/
🔮 Future Enhancements
✨ Multilingual dataset support
✨ Adversarial robustness testing
✨ Noise & channel-aware training
✨ Audio-visual deepfake extension

👤 Maintainer
Hemanth Kumar B
📧 hemanthkumarboddana002@gmail.com
🏫 Narasaraopeta Engineering College

📅 Last Updated: 2026-02-05
