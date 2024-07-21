import streamlit as st

def home():
    import Homepage
    Homepage.render()
              
def About():
    import Aboutpage
    Aboutpage.render()
    
def Bird():
    import Knowpage
    Knowpage.render()


def Info():
    import Getinfopage
    Getinfopage.render()

def Spec():
    import Spectrogrampage
    Spectrogrampage.render()        

def Cont():
    import Contripage
    Contripage.render()
pages = {
    "Home": home ,
    "About" : About , 
    "Know the Bird": Bird,
    "Get Info": Info ,
    "Spectrogram": Spec , 
    "Contribute": Cont 
    
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()) , index=0)
pages[selection]()
    
            
          
    
