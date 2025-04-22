# MFCC-Interpretation

This repository demonstrates a complete walkthrough of **MFCC (Mel-Frequency Cepstral Coefficients)**, a fundamental feature extraction technique in audio signal processing. From raw waveforms to classification use-cases, everything is covered in one interactive file.

---

## 🔧 Features

- Load & visualize waveforms
- Display spectrogram and log-Mel spectrogram
- Extract MFCCs with Delta and Delta-Delta
- 🎯 **Pitch Tracking Overlay**
- 📈 **MFCC-based Classifier** (Speaker Identification / Emotion Recognition)
- 🌍 **Cross-language/Emotion MFCC Comparison**

---

## 📁 Structure

### 1. `mfcc_playground.ipynb`
- Visualize waveform
- Spectrograms
- MFCC extraction & visualization
- Delta and delta-delta computation
- Pitch estimation and overlay
- Emotion or speaker classification using MFCCs (basic model)
- Compare MFCCs from different languages or emotional states

---

## 🧠 What is MFCC?
MFCCs simulate the human auditory system’s perception of sound. They're derived from:

1. **Framing & Windowing** the signal
2. Applying the **FFT** to convert time to frequency domain
3. Applying **Mel filterbanks** to model human hearing
4. Taking the **log** of filterbank energies
5. Applying **DCT (Discrete Cosine Transform)** to get decorrelated features

---

## 🔬 Mathematical Background

### Mel Scale Formula:
\[ m = 2595 \log_{10}\left(1 + \frac{f}{700}\right) \]

### DCT to obtain MFCC:
\[ c_n = \sum_{k=1}^K \log(S_k) \cos\left[\frac{\pi n}{K}(k - 0.5)\right] \]

Where \( S_k \) is the log-energy from Mel filterbank \( k \)

---

## 🎨 Visualizations

- 📈 Waveform
- 🔊 Spectrogram & Mel Spectrogram
- 📉 MFCCs & Delta MFCCs
- 🎯 Pitch Tracking over waveform/MFCCs
- 🌈 Emotion or language-based MFCC visual comparison

---

## 🤖 ML Applications

- 🔊 **Speaker Identification**: Who is speaking?
- 😠 **Emotion Recognition**: What is the emotion conveyed?
- 🌐 **Language Variation**: Compare English, Urdu, Portuguese, etc.

---

## ▶️ Try it!
Run the `mfcc_playground.ipynb` notebook in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](link_to_colab)

---

## 📦 Requirements
```bash
pip install librosa matplotlib numpy sklearn scipy
```

---

## 🙋‍♀️ Who is this for?
Anyone exploring:
- Audio signal processing
- Speech-related ML tasks
- Math-for-ML learners

---

## 📌 To Do / Future Features
- Add CNN classifier for spectrogram inputs
- Integrate with Wav2Vec or Whisper for feature comparison
- Export interactive plots via `plotly`

---



**📚 Related Blog Post**
This repository contains supporting material for my blog post:
👉 Decoding Audio with MFCCs: A Visual & Mathematical Journey

Check out the full article on [Decoding Audio with MFCCs]([https://dsp-01.hashnode.dev/decoding-audio-with-mfccs-a-visual-and-mathematical-journey])

In the blog, I explain what MFCCs are, how to interpret all 13 coefficients, and how to visualize them effectively.
Due to space constraints, some additional comparisons (like emotional or multilingual audio) are only available here in this repo. Feel free to explore and try your own experiments!
