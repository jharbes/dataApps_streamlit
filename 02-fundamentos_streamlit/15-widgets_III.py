import streamlit as st
import pandas as pd
import numpy as np


st.title('Widgets 3rd part')


# https://docs.streamlit.io/library/api-reference/widgets/st.date_input
st.header('Date Input')

import datetime

d = st.date_input(
    "When\'s your birthday",
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.time_input
st.header('Time Input')

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option. For more info on how to set config options, see https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options
st.header('File Uploader')

from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)


'-------------------------------------------------------------'


st.write('Insert a file uploader that accepts multiple files at a time:')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.camera_input
st.header('Camera Input')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)


'-------------------------------------------------------------'

st.warning('To read the image file buffer as bytes, you can use getvalue() on the UploadedFile object.')

img_file_buffer = st.camera_input("Take a picture:")

if img_file_buffer is not None:
    # To read image file buffer as bytes:
    bytes_data = img_file_buffer.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.color_picker
st.header('Color Picker')

# primeira opcao label, segunda opcao cor default
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)