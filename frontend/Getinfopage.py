import streamlit as st
import time
import pandas as pd
import os

def load_data():
    return pd.read_csv('cleaned_data.csv')

def display_options(options):
    selected_option = st.selectbox("Select the Bird", options)
    
    if selected_option:
        with st.spinner("Downloading data..."):
            time.sleep(3) 
        st.session_state.selected = selected_option
        st.session_state.done = True

def display_info(df):
    if 'selected' in st.session_state and st.session_state.selected:
        with st.container():
            st.header(f":green[Name: ] {st.session_state.selected}")
            encoded_query = st.session_state.selected.replace(" ", "%20").replace("'", "%27")
            google_images_url = f"https://www.google.com/search?hl=en&tbm=isch&q={encoded_query}"

            if st.button('Search for Bird Images'):
                st.write(f"[Click here to see images of {st.session_state.selected}]({google_images_url})")
                

            st.write(f":green[ScientificName: ] {df.loc[df['CommonName']==st.session_state.selected,'SciName'].values[0]}")
            
            
            st.write(f":green[Family:  ] {df.loc[df['CommonName']==st.session_state.selected,'Family'].values[0]}")
            
            
            st.write(f":green[About: ] {df.loc[df['CommonName']==st.session_state.selected,'About'].values[0]}")
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sounds_dir = os.path.join(current_dir, '..', 'sounds')
            audio= f"{st.session_state.selected}.mp3"
            mp3_file_path = os.path.join(sounds_dir, audio)
            if os.path.exists(mp3_file_path):
                with open(mp3_file_path, 'rb') as f:
                    audio_bytes = f.read()
                st.audio(audio_bytes, format='audio/mpeg', start_time=0)
            else:
                st.error(f"Audio file not found at path: {mp3_file_path}")
                        
    else:
        st.write("No bird selected yet.")

def render():
    df = load_data()
    options = df['CommonName'].unique()
    if 'done' not in st.session_state:
        st.session_state.done = False
    display_options(options)
    if st.session_state.done:
        display_info(df)

if __name__ == "__main__":
    render()

  