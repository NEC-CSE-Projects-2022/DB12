# 📦 Dataset Title

**TIMIT-TTS Audio Deepfake Detection Dataset**

---

## 🚀 Usage of Dataset

This dataset is designed for **training, validation, and evaluation of audio deepfake detection models**.  
It supports research in **synthetic media forensics** and is particularly well-suited for **speaker embedding–based approaches** such as **ECAPA-TDNN**.

The dataset can be used to:
- Benchmark audio deepfake detection systems  
- Evaluate robustness against multiple TTS generators  
- Compare detection models under reproducible conditions  

---

## 📊 Dataset Information

- **📛 Dataset Name:** TIMIT-TTS Audio Deepfake Detection Dataset  
- **🌐 Source:** Derived from the original TIMIT corpus and synthetic speech generated using multiple Text-to-Speech (TTS) systems  
- **🧠 Domain:** Audio Processing / Speech Forensics  
- **🎯 Task:** Audio Deepfake Detection  
- **🧩 Problem Type:** Binary Classification (Real vs Fake)  
- **📁 File Format:** WAV  
- **🔗 Dataset Link:**   [Download Dataset](https://drive.google.com/drive/folders/1rSkdHOjh1O82u4pFjhPRkM-UN8AtkeO7?usp=sharing)
---
---

## 📈 Dataset Overview

- **📦 Total Records:** ~80,000 audio samples  
- **🏷 Labeled Records:** ~80,000  
- **📚 Classes:**  
  - Real (Human Speech)  
  - Fake (TTS-Generated Speech)  
- **✍ Annotation Type:** Binary labels (Real / Synthetic)  

### 🗂 Dataset Split
- **Train Set:** Used for model training  
- **Validation Set:** Used for hyperparameter tuning and overfitting prevention  
- **Test Set:** Used for final evaluation and reporting  

Each subset contains both real and synthetic audio samples.

---

## ❓ Why This Dataset?

- 🤖 Synthetic speech generated using **12 different TTS models**  
- 🎙 Includes realistic synthesis artifacts and voice variations  
- ⚖ Reflects real-world **class imbalance** scenarios  
- 🔊 Standardized audio format compatible with deep learning pipelines  
- 📊 Enables fair comparison of audio deepfake detection systems  

---

## 🎙 Audio Characteristics

- **Format:** WAV  
- **Sampling Rate:** 16 kHz  
- **Channels:** Mono  
- **Average Duration:** ~3 seconds  
- **Language:** English  

All audio samples are resampled and standardized for consistency.

---

## 🤖 Synthetic Speech Details

The synthetic portion of the dataset is generated using **multiple TTS architectures**, introducing diversity in:
- Speaking styles  
- Voice timbre  
- Pitch and timing  
- Compression artifacts  
- Background noise and post-processing effects  

This helps improve generalization to unseen TTS systems.

---

## 🗣 Real Speech Details

Real speech samples are sourced from the **original TIMIT dataset**, which contains carefully recorded, phonetically rich human speech from multiple speakers.  
These samples serve as ground truth for genuine audio.

---

## 🧩 Features Used

- **Feature 1:** ECAPA-TDNN Speaker Embeddings  
- **Feature 2:** Spectral and prosodic speech characteristics  
- **Feature 3:** Temporal patterns and synthesis artifacts  

---

## 🧠 Summary

The **TIMIT-TTS Audio Deepfake Detection Dataset** is a large-scale dataset created to support research in **audio deepfake detection** and **synthetic media forensics**.  
By combining real speech with diverse synthetic samples generated using multiple TTS systems, the dataset enables robust evaluation of detection models under realistic conditions.

The dataset is intended strictly for **research and academic use**, and proper citation of the original **TIMIT-TTS paper** is required when used in publications.
