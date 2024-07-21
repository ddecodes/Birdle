import streamlit as st 
import time

def render():
    st.title(":green[About]")
    st.write("______________________________________________________________________________________")
    st.write(
        "At BirdChirp AI, our mission is to bridge the gap between technology and nature by offering advanced solutions for bird identification. "
        "We leverage cutting-edge machine learning algorithms to analyze bird chirps and provide accurate predictions on bird species."
    )
    
    st.write(
        "**Our Technology:**\n\n"
        "Our platform utilizes state-of-the-art audio analysis techniques to transform bird chirps into detailed spectrograms. "
        "These visual representations capture the frequency patterns of the chirps, which are then analyzed using sophisticated machine learning models. "
        "Our models have been trained on a diverse dataset of bird sounds to ensure high accuracy and reliability in identifying bird species based on their unique calls."
    )
    st.write(
        "To predict voices or identify different speakers using spectrograms and a Support Vector Classifier (SVC), "
        "we first convert audio signals into spectrograms. Spectrograms are visual representations that illustrate how "
        "the frequency content of the audio varies over time. This process involves generating spectrograms from the audio "
        "and then extracting numerical features from these visualizations. Commonly used features include Mel-Frequency "
        "Cepstral Coefficients (MFCCs), which capture the timbral texture of the audio, along with additional features "
        "such as chroma features and spectral contrast."
    )
    
    st.write(
        "Once we have extracted these features, we proceed to train an SVC model. The training phase utilizes a dataset "
        "in which each audio sample is represented by its features and labeled according to the specific speaker or voice "
        "characteristic. The SVC model learns to classify these features into different categories based on the provided labels."
    )
    
    st.write(
        "After training the model, we can use it to predict new voices. For this purpose, we extract the same features from "
        "a new audio sample and input these features into the trained SVC model. The model then predicts the class, such as "
        "the speaker’s identity, based on the input features. This approach integrates the detailed frequency analysis offered "
        "by spectrograms with the powerful classification capabilities of SVC, enabling us to effectively identify and predict different voices."
    )
    st.write(
        "WELCOME TO THE COMMUNITY....."
    )
    st.write("___________________________________________________________________________")