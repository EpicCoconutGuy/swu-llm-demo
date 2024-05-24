import streamlit as st

if "notification" not in st.session_state:
        st.session_state["notification"] = False

if "sound" not in st.session_state:
     st.session_state["sound"] = 50

if "appearance" not in st.session_state:
     st.session_state["appearance"] = "Dark"

with st.form("settings_form"):
     noti = st.toggle(label="Recieve Notification", key="notification")
     sound = st.slider("Volume", min_value=0, max_value=100, key="sound")
     appearance = st.selectbox("Appearance", ["Dark", "Light"] ,index=0 if st.session_state["appearance"] == "Dark" else 1, key="appearance")
     submit = st.form_submit_button("Save Change")
     
st.write(st.session_state)