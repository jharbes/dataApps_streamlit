import streamlit as st

st.title('This is a st.title')

# observe que os dois asteristicos (**) deixa o texto em negrito
st.markdown('Example of **st.markdown**') 

st.header('Exemplo de st.header')

st.subheader('Adicionando um st.subheader')

# st.caption funciona bem para legendas
st.caption('Testando o st.caption')

# bom para trechos de código, já vem com a opção de copiar para a área de transferencia no canto superior direito
st.code('''Bom para colocar trexos de código\nTestando
observe o pulo de linha''')
st.code('Outro bloco')

# Exemplo de st.text, texto sem formatação
st.text('Olá Mundo com st.text')

# texto com formato em LaTeX
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
    ''')