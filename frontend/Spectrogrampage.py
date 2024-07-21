import streamlit as st
import librosa
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import librosa.display
def render():
    st.header(":green[Spectrogram :]")
    st.write("A spectrogram is a visual representation of the spectrum of frequencies in a signal as it varies with time. It provides a way to visualize how the frequencies in an audio signal change over time, which is particularly useful for analyzing and understanding audio signals in various fields such as speech processing, music analysis, and bioacoustics.")
    def extract_features(audio_bytes):
        audio = BytesIO(audio_bytes)
        y, sr = librosa.load(audio, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_scaled = np.mean(mfccs.T, axis=0)
        return mfccs_scaled, y, sr
    uploaded_files = st.file_uploader("Choose an MP3 file", type="mp3", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
            if(len(uploaded_files)==1):
                if uploaded_file is not None:
                    audio_bytes = uploaded_file.read()
                    features, y, sr = extract_features(audio_bytes)
                    fig, ax = plt.subplots()
                    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
                    librosa.display.specshow(librosa.power_to_db(S, ref=np.max), sr=sr, x_axis='time', y_axis='mel', ax=ax)
                    ax.set_title('Mel-frequency spectrogram')
                    st.pyplot(fig)
                    st.audio(audio_bytes, format="audio/mp3")
        
    
                    
            else:
                st.write("Remove the first file")        
            