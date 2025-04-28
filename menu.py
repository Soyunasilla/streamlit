import streamlit as st
st.sidebar.write('Menu')
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)
st.title('Cambio')
st.write('am')
