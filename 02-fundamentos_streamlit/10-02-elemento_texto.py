import streamlit as st

st.title("App Streamlit")
st.markdown("Streamlit é **divertido**.")
st.header("Adicionando um cabeçalho")
st.subheader("Adicionando um subcabeçalho")
st.caption("O texto está pequeno")
st.code("v=Fulano")
st.text("Olá mundo")
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')