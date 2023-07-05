import streamlit as st


st.title('Media Elements')

'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/media/st.image
st.header('Adding Images')

from PIL import Image

image = Image.open('../media/TECHNIPFMC.jpg')

st.image(image, caption='TechnipFMC')



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/media/st.audio
st.header('Audio')

import numpy as np

audio_file = open('../media/mpthreetest.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/media/st.video
st.header('Video')

video_file = open('../media/sample-5s.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)