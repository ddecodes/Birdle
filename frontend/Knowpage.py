import streamlit as st 
import pickle
import os
import librosa
import numpy as np
from io import BytesIO
import pandas as pd
df = pd.read_csv('cleaned_data.csv')
def render():
    
    st.header("Upload the audio and we will predict the bird for you..")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'model.pkl')
    label_path = os.path.join(current_dir, '..', 'label_encoder.pkl')
    scaler_path = os.path.join(current_dir, '..', 'scaler.pkl')
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(label_path, 'rb') as label_file:
        l = pickle.load(label_file)
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
      
    def extract_features(audio_bytes):
        audio = BytesIO(audio_bytes)
        y, sr = librosa.load(audio, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_scaled = np.mean(mfccs.T, axis=0)
        return mfccs_scaled


    uploaded_files = st.file_uploader("Choose an MP3 file", type="mp3", accept_multiple_files=True)
    

    for uploaded_file in uploaded_files:
        if(len(uploaded_files)==1):
            audio_bytes = uploaded_file.read()
            features = extract_features(audio_bytes)
            features = features.reshape(1, -1)
            features = scaler.transform(features)
            prediction = model.predict(features)
            predicted_label = l.inverse_transform(prediction)[0]
            st.header(f":green[Predicted :] {predicted_label}")
            st.audio(audio_bytes, format="audio/mp3")
            with st.container():
                st.header(f":green[Name: ] {predicted_label}")
                encoded_query = predicted_label.replace(" ", "%20").replace("'", "%27")
                google_images_url = f"https://www.google.com/search?hl=en&tbm=isch&q={encoded_query}"

                if st.button('Search for Images'):
                    st.write(f"[Click here to see images of {predicted_label}]({google_images_url})")
                    

                st.write(f":green[ScientificName: ] {df.loc[df['CommonName']==predicted_label,'SciName'].values[0]}")
                
                
                st.write(f":green[Family:  ] {df.loc[df['CommonName']==predicted_label,'Family'].values[0]}")
                st.write(f":green[About:  ] {df.loc[df['CommonName']==predicted_label,'About'].values[0]}")
        else:
            st.write("Remove the first file")        
            
        
