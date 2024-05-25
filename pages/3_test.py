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
st.markdown("## test")
with st.container(height=180, border=True):
    logoCol, loginCol= st.columns([60,40])
    with logoCol:
        logoPic = st.image("https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg", width=300)
    with loginCol:
        st.header("Welcome to swu llm app")
        loginButton = st.button("COntinue without login",use_container_width=True, help="Login")
        if loginButton:
            st.switch_page("###")
