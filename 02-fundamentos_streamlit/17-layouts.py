import streamlit as st
import time


st.title('Layouts and Containers')


'-------------------------------------------------------------'


# https://docs.streamlit.io/library/api-reference/layout/st.sidebar

with st.sidebar:
    st.header('Sidebar')
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(2)
    st.success("Done!")

    '-------------------------------------------------------------'

# Here's an example of how you'd add a selectbox and a radio button to your sidebar:

# observe que mesmo nao estando no mesmo with do sidebar inicial eles foram incluidos no sidebar, importante notar que para organizacao melhor inclui-los todos abaixo do mesmo with

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    st.warning("The only elements that aren't supported using object notation are st.echo and st.spinner. To use these elements, you must use with notation.")



#'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/layout/st.columns
st.header('Columns')

st.warning('Columns cannot be placed inside other columns in the sidebar. This is only possible in the main area of the app.')

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")


'-------------------------------------------------------------'


import numpy as np

# observe que estamos setando a proporcao da largura entre as colunas
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/layout/st.tabs
st.title('Tabs') # utilizando abas

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)



'-------------------------------------------------------------'



# https://docs.streamlit.io/library/api-reference/layout/st.expander
st.header('Expander')

st.warning('Currently, you may not put expanders inside another expander.')

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

# o expander gera uma nota explicativa para um grafico ou outra situacao qualquer, aqui o expander explica sobre os dados serem aleatorios

st.write('Expander usando o with')

# You can use with notation to insert any element into an expander
with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")


'-------------------------------------------------------------'


# Or you can just call methods directly in the returned objects:

st.write('Expander sem usar o with')

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

expander = st.expander("See explanation")
expander.write("""
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
    be random.
""")
expander.image("https://static.streamlit.io/examples/dice.jpg")