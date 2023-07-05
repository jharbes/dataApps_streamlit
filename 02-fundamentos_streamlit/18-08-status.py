import time
import streamlit as st

st.header("Utilizando Barra de Progresso")

my_bar = st.progress(0)

for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)

st.header("Utilizando o Spinner")

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.header("Utilizando o Ballons")

st.balloons()

st.header("Utilizando o Snowflake")

st.snow()

st.header("Utilianzdo Mensagens")

st.error('This is an error')

st.warning('This is a warning')

st.info('This is a purely informational message')

st.success('This is a success message!')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)