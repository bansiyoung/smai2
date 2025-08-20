import streamlit as st

st.sidebar.markdown("Clicked Page 7")

st.title("page 7")

picture=st.camera_input("Take a pictue")

if picture:
    st.image(picture)