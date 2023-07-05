import streamlit as st
import time


# https://docs.streamlit.io/library/api-reference/status
st.title('Status Elements')


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/status/st.progress
st.header('Progress Bar')

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1, text=progress_text)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/status/st.spinner
st.header('Spinner')

with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')



'-------------------------------------------------------------'



st.header('Balloons')

st.balloons()



'-------------------------------------------------------------'



st.header('Snowflake')

st.snow()



'-------------------------------------------------------------'



st.header('Error message')

st.error('This is an error', icon="🚨")



'-------------------------------------------------------------'



st.header('Warning message')

st.warning('This is a warning', icon="⚠️")



'-------------------------------------------------------------'



st.header('Info message')

st.info('This is a purely informational message', icon="ℹ️")



'-------------------------------------------------------------'



st.header('Sucess message')

st.success('This is a success message!', icon="✅")



'-------------------------------------------------------------'



st.header('Exception Output')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)