import streamlit as st
import pandas as pd
import numpy as np

# https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# funciona como o dropdown
st.header('Select Box')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/widgets/st.multiselect
st.header('Multiselect')

options = st.multiselect(
    'What are your favorite colors?',

    ['Green', 'Yellow', 'Red', 'Blue'],

    # essa linha abaixo de opções mostra as opções default (as que já vem marcado quando o multiselect é carregado)
    ['Yellow', 'Red'])

st.write('You selected:', options)


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/widgets/st.slider
st.header('Slider')

st.write('Range Slider')
# (label, valor_inicial, valor_final, valor_default)
age = st.slider('How old are you?', 0, 130, 25)

st.write("I'm ", age, 'years old')

'-------------------------------------------------------------'
from datetime import datetime

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/widgets/st.select_slider
st.header('Select Slider')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)