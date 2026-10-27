import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="JTG OA Lab",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0.6rem 0.6rem 0 0.6rem; max-width: 100%;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.link_button("📱 Open full screen (best on mobile)", "app/static/index.html")

components.iframe("app/static/index.html", height=1100, scrolling=True)
