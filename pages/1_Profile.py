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
st.markdown("## Profile")
with st.form("form"):
    with st.container(height=180, border=False):
        imageCol, inputCol= st.columns([25, 60])
        uploaded_file = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
        with imageCol:
            profilePic = st.image(uploaded_file, width=180)
        with inputCol:
            st.container(height=10, border=False)
            uploaded_file = st.file_uploader("Upload a file")
            if uploaded_file is not None:
                profilePic.image(uploaded_file, width=180)

    #(r"$\textsf{\Large Username}$")
    usernameValue = st.text_input(label="Username", value=st.session_state["username"])
    roleselectValue = st.selectbox(label="Role", options=["Student", "Teacher"], index=0 if st.session_state["role"] == "Student" else 1)

    submit = st.form_submit_button("Save Changes")
if submit:
    st.session_state["username"] = usernameValue
    st.session_state["role"] = roleselectValue

st.write(st.session_state)
