import streamlit as st
import pandas as pd
import numpy as np

# https://docs.streamlit.io/library/api-reference/widgets
st.title('Input Widgets')

'-------------------------------------------------------------'

# https://docs.streamlit.io/library/api-reference/widgets/st.button
st.header('Button')
st.caption('Display a button widget')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')



'-------------------------------------------------------------'

# https://docs.streamlit.io/library/api-reference/widgets/st.download_button
st.header('Download Button')

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

my_large_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)