from google.colab import files
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd

print("\n🔁 Upload a happy audio file to compare MFCCs")
uploaded = files.upload()
happy = list(uploaded.keys())[0]
y, sr = librosa.load(happy)

# Listen to audio
print("🔊 Playing example audio...")
ipd.display(ipd.Audio(y, rate=sr))

# Compute MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Plot MFCC heatmap
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC (13 coefficients)')
plt.tight_layout()
plt.show()

# Show each MFCC coefficient separately
plt.figure(figsize=(12, 10))
for i in range(13):
    plt.subplot(7, 2, i + 1)
    plt.plot(mfccs[i])
    plt.title(f'MFCC Coefficient {i+1}')
    plt.tight_layout()
plt.show()

# 👂 Simulate listening to each coefficient
print("\n🎧 Simulated Audio from Each Individual MFCC Coefficient")
for i in range(13):
    isolated = np.zeros_like(mfccs)
    isolated[i] = mfccs[i]  # only keep 1 coefficient
    
    # Reconstruct the audio from isolated MFCC
    audio_approx = librosa.feature.inverse.mfcc_to_audio(isolated, sr=sr)
    print(f"\n🎵 MFCC Coefficient {i+1}")
    ipd.display(ipd.Audio(audio_approx, rate=sr))
