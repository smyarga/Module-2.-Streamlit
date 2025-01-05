import streamlit as st

st.header('My first app')

if st.button('Say hello'):
    st.write('Goodbye')
else:
    st.write('Just ordinary button')