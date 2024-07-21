import streamlit as st
import time
from navigation import pages

def landing():
    with st.container():
        st.image("Landing Page.jpg")
        col1, col2 = st.columns([0.7, 2])
        with col2:
            st.header(":orange-background[WELCOME TO BIRDLE]")
    
    progress_text = "Loading...."
    my_bar = st.progress(0, text=progress_text)

    for i in range(100):
        time.sleep(0.01)
        my_bar.progress(i + 1, text=progress_text)

    time.sleep(1)
    my_bar.empty()
    st.session_state.loading_complete = True
    st.rerun()



def main():
    if 'loading_complete' not in st.session_state:
        st.session_state.loading_complete = False
    if st.session_state.loading_complete:
        selection = st.sidebar.radio("Go to", list(pages.keys()), index=0)
        pages[selection]()
    else:
        landing()

if __name__ == "__main__":
    main()
     





  
