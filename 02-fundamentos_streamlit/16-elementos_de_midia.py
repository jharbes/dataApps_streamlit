import streamlit as st


st.title('Media Elements')

'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/media/st.image
st.header('Image')

from PIL import Image

image = Image.open('../media/TECHNIPFMC.jpg')

st.image(image, caption='Sunrise by the mountains')