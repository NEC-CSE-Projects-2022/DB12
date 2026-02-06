---

## 📦 Dataset Used

👉 **TIMIT-TTS Audio Deepfake Detection Dataset**  
🔗 [Download Dataset](https://drive.google.com/drive/folders/1rSkdHOjh1O82u4pFjhPRkM-UN8AtkeO7?usp=sharing)

---

## 📊 Dataset Description

The dataset used in this project is derived from the **TIMIT-TTS corpus**, a large-scale synthetic speech dataset created to support research in **audio deepfake detection** and **synthetic media forensics**. Due to its large size, the dataset is hosted on **Google Drive** instead of GitHub.

This dataset contains a combination of **real human speech** and **synthetic speech generated using multiple Text-to-Speech (TTS) systems**, making it highly suitable for training and evaluating deepfake detection models.

---

## 🗂 Dataset Organization

The dataset is structured into three standard subsets to support proper machine learning experimentation:

- **Train Dataset**  
  Used to train the deepfake detection model.  
  Contains the largest portion of real and synthetic samples.

- **Validation Dataset**  
  Used for hyperparameter tuning, threshold selection, and preventing overfitting.

- **Test Dataset**  
  Used exclusively for final performance evaluation and result reporting.

Each subset includes both **real** and **fake (TTS-generated)** audio samples.

---

## 🎙 Audio Characteristics

- **Audio Format:** WAV  
- **Sampling Rate:** 16 kHz  
- **Channels:** Mono  
- **Average Duration:** ~3 seconds per sample  
- **Language:** English  

All audio samples are resampled and standardized to ensure compatibility with **ECAPA-TDNN** speaker embedding extraction.

---

## 🤖 Synthetic Speech Details

The synthetic portion of the dataset was generated using **12 different Text-to-Speech (TTS) models**, covering a wide variety of synthesis techniques and voice characteristics. This diversity introduces realistic deepfake artifacts and variations, helping the detection model generalize better to unseen TTS systems.

Synthetic samples may include variations such as:

- Different speaking styles  
- Voice timbre changes  
- Compression artifacts  
- Pitch and timing variations  
- Background noise and post-processing effects  

---

## 🗣 Real Speech Details

The real speech samples originate from the **original TIMIT dataset**, which contains phonetically rich and carefully recorded human speech from multiple speakers. These samples serve as the ground truth for genuine human audio.

---

## 📈 Dataset Scale (Approximate)

- **Total Audio Samples:** ~80,000  
- **Number of Speakers:** 37  
- **Real Samples:** ~6,600  
- **Synthetic Samples:** ~73,000  
- **TTS Models Used:** 12  

This class imbalance reflects real-world scenarios where synthetic audio can be generated at scale.

---

## 🎯 Purpose of the Dataset

This dataset is designed to:

- Benchmark **audio deepfake detection systems**
- Evaluate robustness against multiple TTS generators
- Support research in **speaker embedding-based detection**
- Enable reproducible and fair comparisons between detection models

---

## 🔐 Ethical Considerations

- The dataset contains **only synthetic or publicly available speech**
- No personal, sensitive, or identifiable user data is included
- Intended strictly for **research and academic purposes**

---

## 📌 Notes

- The dataset is not included directly in this repository due to size limitations.
- Users must download it separately from Google Drive.
- Proper citation of the original **TIMIT-TTS paper** is required when using this dataset in publications.



---
