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
else: pass

if "role" in st.session_state:
    st.session_state["role"] = st.session_state["role"]
else: pass

#start
st.markdown("<h2 style='text-align: center;'>Question 1</h2>", unsafe_allow_html=True)

toolBar_Col, main_Col= st.columns([1, 13])
with toolBar_Col:
    powerup1 = st.button("🆙", use_container_width=True, key="1")
    powerup2 = st.button("🆙", use_container_width=True, key="2")
    powerup3 = st.button("🆙", use_container_width=True, key="3")
    powerup4 = st.button("🆙", use_container_width=True, key="4")
    powerup5 = st.button("🆙", use_container_width=True, key="5")
    st.divider()
    profileButton = st.button("🙍‍♂️", use_container_width=True, help="Profile")
    exitButton = st.button("🚪", use_container_width=True, help="Exit")
    settingsButton = st.button("⚙️", use_container_width=True, help="Settings")
    if profileButton:
        st.switch_page("pages/1_Profile.py")
    if settingsButton:
        st.switch_page("pages/3_Settings.py")

with main_Col:
    with st.container(height=255,border=True):
        st.markdown("### QUESTION HERE")
    with st.container(border=True):
        answer1 = st.button("Answer 1", use_container_width=True)
        answer2 = st.button("Answer 2", use_container_width=True)
        answer3 = st.button("Answer 3", use_container_width=True)
        answer4 = st.button("Answer 4", use_container_width=True)

    back_Col, next_Col= st.columns([1, 1])
    with back_Col:
        st.button("⬅️ Back", use_container_width=True, key="back")
    with next_Col:
        st.button("Next ➡️", use_container_width=True, key="next")

st.write(st.session_state)