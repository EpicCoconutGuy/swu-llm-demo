import streamlit as st

#load settings
if "notification" in st.session_state:
    st.session_state["notification"] = st.session_state["notification"]
else: st.session_state["notification"] = True

if "sound" in st.session_state:
    st.session_state["sound"] = st.session_state["sound"]
else: st.session_state["sound"] = 50

if "appearance" in st.session_state:
    st.session_state["appearance"] = st.session_state["appearance"]
else: st.session_state["appearance"] = "Dark"

if "username" in st.session_state:
    st.session_state["username"] = st.session_state["username"]
else: pass

if "role" in st.session_state:
    st.session_state["role"] = st.session_state["role"]
else: pass

#start
st.markdown("## Settings")
with st.form("settings_form"):
     noti = st.toggle(label="Recieve Notification", value=st.session_state["notification"])
     sound = st.slider(label="Volume", min_value=0, max_value=100, value=st.session_state["sound"])
     theme = st.selectbox(label="Appearance", options=["Dark", "Light"] ,index=0 if st.session_state["appearance"] == "Dark" else 1)
     submit = st.form_submit_button("Save Changes")
if submit:
     st.session_state["notification"] = noti
     st.session_state["sound"] = sound
     st.session_state["appearance"] = theme


st.write(st.session_state)