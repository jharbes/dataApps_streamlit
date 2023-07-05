import streamlit as st
import pandas as pd
import numpy as np


st.title('Widgets 2nd part')


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


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/widgets/st.text_input
st.header('Text input')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

'-------------------------------------------------------------'

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.number_input
st.header('Number input')

number = st.number_input('Insert a number')
st.write('The current number is ', number)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/widgets/st.text_area
st.header('Text Area')

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''',height=300) # altura alterada
st.write('Sentiment:', txt)