import streamlit as st
import pandas as pd
import numpy as np


# grafico de linha simples
# https://docs.streamlit.io/library/api-reference/charts/st.line_chart
st.header('Gráfico SIMPLES Line Chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)




# grafico de area simples
# https://docs.streamlit.io/library/api-reference/charts/st.area_chart
st.header('Gráfico SIMPLES de Área (AreaChart)')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)




# grafico de barras simples
# https://docs.streamlit.io/library/api-reference/charts/st.bar_chart
st.header('Gráfico SIMPLES de Barras (BarChart)')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)




# grafico de mapa (scatterplot)
# https://docs.streamlit.io/library/api-reference/charts/st.map
st.header('Gráfico de mapa (scatterplot)')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)




# graficos com matplotlib
# https://docs.streamlit.io/library/api-reference/charts/st.pyplot
st.header('Gráfico com MATPLOTLIB')

import matplotlib.pyplot as plt

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)




# graficos com altair (muito bem detalhados no outro curso de streamlit)
# https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
st.header('Gráficos com ALTAIR')

import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)




# graficos com vega_lite
# https://docs.streamlit.io/library/api-reference/charts/st.vega_lite_chart
st.header('Gráficos com VEGA LITE')

from vega_datasets import data

chart_data = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(chart_data, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

'--------------------------------------------------------'

st.header('Gráficos com VEGA LITE 2')
source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )




# graficos com plotly
# https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
st.header('Gráficos com PLOTLY')

import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


'--------------------------------------------------------'

st.header('Gráficos com PLOTLY 2')

import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)




# graficos com Bokeh (possui boas opções de salvar, zoom, etc)
# https://docs.streamlit.io/library/api-reference/charts/st.bokeh_chart
# https://bokeh.pydata.org/

st.header('Gráficos com Bokeh')
st.markdown('Importante notar que o Streamlit suporta apenas a **versão 2.4.3** do Bokeh')

from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)




# graficos com PyDeck
# https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart
# https://deckgl.readthedocs.io/en/latest/

st.header('Gráficos com PyDeck')

import pydeck as pdk

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))




# GRAFOS com GraphViz
# https://docs.streamlit.io/library/api-reference/charts/st.graphviz_chart

st.header('GRAFOS com GraphViz')

import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')