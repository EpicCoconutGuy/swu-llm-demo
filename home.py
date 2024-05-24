from backend import ChatGPT
from settings import settings_menu
import streamlit as st


st.markdown("<h2 style='text-align: center;'>Question 1</h2>", unsafe_allow_html=True)

toolBar_Col, main_Col= st.columns([1, 13])
with toolBar_Col:
    st.button("🆙", use_container_width=True, key="powerup1")
    st.button("🆙", use_container_width=True, key="powerup2")
    st.button("🆙", use_container_width=True, key="powerup3")
    st.button("🆙", use_container_width=True, key="powerup4")
    st.button("🆙", use_container_width=True, key="powerup5")
    st.divider()
    st.button("🙍‍♂️", use_container_width=True, help="Profile", key="profile")
    st.button("🚪", use_container_width=True, help="Exit", key="exit")
    st.button("⚙️", use_container_width=True, help="Settings", on_click=settings_menu, key="settings")

with main_Col:
    with st.container(height=255,border=True):
        st.markdown("### QUESTION HERE")
    with st.container(border=True):
        st.button("Answer 1", use_container_width=True, key="answer1")
        st.button("Answer 2", use_container_width=True, key="answer2")
        st.button("Answer 3", use_container_width=True, key="answer3")
        st.button("Answer 4", use_container_width=True, key="answer4")

    back_Col, next_Col= st.columns([1, 1])
    with back_Col:
        st.button("⬅️ Back", use_container_width=True, key="back")
    with next_Col:
        st.button("Next ➡️", use_container_width=True, key="next")