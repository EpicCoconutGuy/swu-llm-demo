import streamlit as st

#load settings
if "notification" in st.session_state:
    st.session_state["notification"] = st.session_state["notification"]
else: pass

if "sound" in st.session_state:
    st.session_state["sound"] = st.session_state["sound"]
else: pass

if "appearance" in st.session_state:
    st.session_state["appearance"] = st.session_state["appearance"]
else: pass

if "username" in st.session_state:
    st.session_state["username"] = st.session_state["username"]
else: st.session_state["username"] = ""

if "role" in st.session_state:
    st.session_state["role"] = st.session_state["role"]
else: st.session_state["role"] = "Student"

#start
st.markdown("<h2 style='text-align: center;'>Logopic 1</h2>", unsafe_allow_html=True)

toolBar_Col, main_Col= st.columns([1,13])
with toolBar_Col:
    profileButton = st.button("🙍‍♂️", use_container_width=True, help="Profile")
    settingsButton = st.button("⚙️", use_container_width=True, help="Settings")
    if profileButton:
        st.switch_page("pages/1_Profile.py")
    if settingsButton:
        st.switch_page("pages/2_Settings.py")

with main_Col:

