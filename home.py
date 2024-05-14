from backend import chatGPT
import streamlit as st


st.sidebar.container(height=100, border=True)

col1, col2 = st.columns([1, 1])
st.column_config.Column(["1", "2"])