import streamlit as st


with st.form("form"):
    with st.container(height=750, border=True):
        st.header("My profile")
        st.divider()
        
        frontPad, profileCol, characterCol= st.columns([5,60,35])
        with profileCol:
            st.container(height=10, border=False)
            with st.container(height=220, border=False):
                imageCol, inputCol, backPad= st.columns([25, 60, 5])
                uploaded_file = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg"
                with imageCol:
                    profilePic = st.image(uploaded_file, width=180)
                with inputCol:
                    st.container(height=10, border=False)
                    uploaded_file = st.file_uploader("Upload a file")
                    if uploaded_file is not None:
                        profilePic.image(uploaded_file, width=180)
            usernameValue = st.text_input(r"$\textsf{\Large Username}$")
            st.divider()
            roleselectValue = st.selectbox(r"$\textsf{\Large Role}$", ["Student", "Teacher"])

        with characterCol:
            with st.container(height=560, border=True):
                charCol, backPad= st.columns([1, 1000])
                with charCol:
                    st.image("https://www.freeiconspng.com/thumbs/human-icon-png/download-link-for-eps--svg-or-file--0.png", width=500)

    submit = st.form_submit_button("Save Changes")
    
print(usernameValue)
print(roleselectValue)
print(uploaded_file)

