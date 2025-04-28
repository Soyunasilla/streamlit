import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write('Menu')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    1.0, 100.0, (25.0, 75.0)
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.title('BACO')
st.write('Propuesta de Dashboard Movil')

dataframe = pd.DataFrame(
    np.random.randn(1, 6),
    columns=('col %d' % i for i in range(56)))

st.dataframe(dataframe.style.highlight_max(axis=0))

x = st.slider('x') # 👈 este es un widget
st.write(x, 'al cuadrado es', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name
