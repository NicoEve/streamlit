import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green', 'Black', 'White',
     'Purple', 'Yellow', 'Orange'))

st.write('Your favorite color is ', option)