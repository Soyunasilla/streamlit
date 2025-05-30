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
    columns=[f'AM {i}' for i in range(10)]
)

st.dataframe(dataframe)
x = st.slider('x') # 👈 este es un widget
st.write(x, 'al cuadrado es', x * x)

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

from PIL import Image, ImageDraw, ImageFont

image = Image.open('streamlit.jpeg')
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
draw.text((10, 10), "Zombies!", fill=(255, 0, 0), font=font)

st.image(image, caption='Zombies vs Guerrera Ninja')

# Abres el archivo OGG en modo binario
with open('myaudio.ogg', 'rb') as audio_file:
    audio_bytes = audio_file.read()

# Aquí Streamlit muestra el player
st.audio(audio_bytes, format='audio/ogg')

video_file = open('mi_video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

import qrcode

# Tus tres cadenas
datos = [
    "4,399wn3kcCMJCTCTDPQJ",
    "4,4rru3r56CMJCTCTDPQJ",
    "4,rr8cukr9CMJCTCTDPQJ"
]

# Opciones de diseño (opcional)
qr_opts = {
    'version': None,       # ajusta automáticamente el tamaño
    'error_correction': qrcode.constants.ERROR_CORRECT_M,
    'box_size': 10,        # tamaño de cada “cuadrito”
    'border': 4,           # ancho del borde (en cuadros)
}

for idx, texto in enumerate(datos, start=1):
    qr = qrcode.QRCode(**qr_opts)
    qr.add_data(texto)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    nombre = f"qr_{idx}.png"
    img.save(nombre)
    print(f"Guardado → {nombre}")
