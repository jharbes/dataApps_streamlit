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


