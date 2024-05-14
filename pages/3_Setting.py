import streamlit as st

with st.container(height=750, border=True):
    st.header("Setting")
    st.divider()
    with st.container(height=250, border=False):
            notiCol, inputCol, backPad= st.columns([20,10, 45])
            with notiCol:
                 st.write("Notification")
            with inputCol:
                 st.button("Get a Notification", use_container_width=True)
    st.write("Sound")           
    loud = st.slider('SFX', min_value=0, max_value=100)

    with st.container(height=250, border=False):
            appCol, blackCol, backPad= st.columns([20,10, 45])
            with notiCol:
                 st.write("Appearance")
            with inputCol:
                 st.button("Light Mode", use_container_width=True) #ต้องทำlight mode


st.button("Save change")