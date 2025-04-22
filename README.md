# MFCC-Interpretation

This repository demonstrates a complete walkthrough of **MFCC (Mel-Frequency Cepstral Coefficients)**, a fundamental feature extraction technique in audio signal processing. From raw waveforms to classification use-cases, everything is covered in one interactive file.

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

## 🤖 ML Applications

- 🔊 **Speaker Identification**: Who is speaking?
- 😠 **Emotion Recognition**: What is the emotion conveyed?
- 🌐 **Language Variation**: Compare English, Urdu, Portuguese, etc.

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
- Basic Audio Feature learners

---

**This code will**

Ask for an audio file

Show the MFCC heatmap

Play audio synthesized from each of the 13 MFCCs individually

Show an interpretation for each one

    0: "Low freq. energy - pitch, loudness",
    1: "General spectral slope",
    2: "Changes in pitch",
    3: "Energy variation",
    4: "Middle freq. textures",
    5: "Consonant shape hints",
    6: "Voicing info",
    7: "Noise / fricatives",
    8: "Tonal purity",
    9: "Roughness or grain",
    10: "Energy fluctuation",
    11: "High-freq dynamics",
    12: "Noise floor variations"

---

**📚 Related Blog Post**
This repository contains supporting material for my blog post:

👉 Decoding Audio with MFCCs: A Visual & Mathematical Journey

Check out the full article on [Decoding Audio with MFCCs(https://dsp-01.hashnode.dev/decoding-audio-with-mfccs-a-visual-and-mathematical-journey)]

In the blog, I explain what MFCCs are, how to interpret all 13 coefficients, and how to visualize them effectively.
Due to space constraints, some additional comparisons (like emotional or multilingual audio) are only available here in this repo. Feel free to explore and try your own experiments!
