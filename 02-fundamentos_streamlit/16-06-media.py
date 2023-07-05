import streamlit as st
from PIL import Image

st.header("Adicionando Imagens")

image = Image.open('Recursos/índice.jpg')

st.image(image, caption='Imagem do Curso de Assistente Virtual')

image = Image.open('Recursos/índice2.jpg')

st.image(image, caption='Imagem do Curso Desenvolvimento Web com Flask')

st.header("Adicionando Audio")

audio_file = open('Recursos/test.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

st.header("Adicionando Video")

video_file = open('Recursos/Novo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)