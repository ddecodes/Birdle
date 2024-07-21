import streamlit as st 

def render():
    
    st.title(":green[Get Started]")
    st.header(":green[Birdle]: Unveiling the Symphony of Nature")
    col1 , col2 = st.columns([1,0.3])
    with col1:
            st.image("1st image landing page.jpg")
    with col2:
            st.header("Birdle")
            st.write("An innovative platform designed to enrich your connection with nature by enabling you to identify birds through their unique chirps")
    st.header("     ")     
    col1 , col2 = st.columns([0.3,1])
    with col1:
        st.header(":green[Explore Our GALLERY]")
        st.write("At Birdle, we offer a comprehensive gallery where you can easily access and listen to the chirps , know about the species and habitat of different bird species with a few key strokes.")   
    with col2:
        st.image("2nd image landing page.png")
        st.header("     ")     
    col1 , col2 = st.columns([1,0.3])
    with col1:
        st.image("3rd image landing page.jpg")    
    with col2:
        st.header(":green[Visualize]")
        st.write("At Birdle, we provide advanced visual tools to enrich your auditory experience. You can access detailed spectrograms for each bird chirp in our database")  
    st.header("     ")     
    col1 , col2 = st.columns([0.3,1])
    with col1:
        st.header(":green[Share]")
        st.write("Join our community-driven effort to expand Birdle's collection by contributing your own bird audio recordings. By sharing your recordings, you help enrich our database")
    with col2:    
        st.image("4th image landing page.jpg") 
    st.write("_________________________________________________________________________________________________________________")    