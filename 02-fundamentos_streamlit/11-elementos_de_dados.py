import streamlit as st
import pandas as pd
import numpy as np


"""
As mais variadas opções de display de data estão em:
https://docs.streamlit.io/library/api-reference/data

"""


# display de dataframe (tabela dinamica)
# diversas opcoes em: https://docs.streamlit.io/library/api-reference/data/st.dataframe
st.header('Utilizando Dataframe')
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)




# display de table (tabela estatica)
# opcoes em https://docs.streamlit.io/library/api-reference/data/st.table
st.header('Utilizando Table')
df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.table(df)  




# display de metric
# opcoes em https://docs.streamlit.io/library/api-reference/data/st.metric
st.header('Utilizando Metric')

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")



col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")




# forma de mostrar json na tela
# opcoes em https://docs.streamlit.io/library/api-reference/data/st.json
st.header('Utilizando JSON')

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})