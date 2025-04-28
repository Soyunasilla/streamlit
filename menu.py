import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.write('Menu')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.title('BACO')
st.write('Propuesta de Dashboard Movil')

dataframe = pd.DataFrame(
    np.random.randint(1, 57, size=(6, 10)),
    columns=[f'col {i}' for i in range(10)]
)

st.dataframe(dataframe)
x = st.slider('x') # 👈 este es un widget
st.write(x, 'al cuadrado es', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

from PIL import Image
image = Image.open('streamlit.jpeg')
st.image(image, caption='Zombies')
