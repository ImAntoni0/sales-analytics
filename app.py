import pandas as pd

import streamlit as st

import plotly.express as px

from analysis import analizar_categorias, analizar_subcategorias, analizar_productos, analizar_productos_perdidas

df = pd.read_excel("sample_superstore.xls")

resultado_categorias = analizar_categorias(df)

resultado_subcategorias = analizar_subcategorias(df)

resultado_productos = analizar_productos(df)

resultado_productos_perdidas = analizar_productos_perdidas(df)

st.title("Sales Analytics Dashboard")

st.write("Exploración y análisis de datos de ventas")

st.subheader("Indicadores generales")

ventas_totales = resultado_categorias["Sales"].sum()

ganancias_totales = resultado_categorias["Profit"].sum()

unidades_totales = resultado_categorias["Quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Ventas totales", ventas_totales, format="$%,.2f")
col2.metric("Ganancias totales", ganancias_totales, format="$%,.2f")
col3.metric("Unidades vendidas", unidades_totales, format="%,.0f")

st.subheader("Análisis de rentabilidad por categoría")

st.dataframe(resultado_categorias)

st.subheader("Análisis de rentabilidad por subcategoría")

st.dataframe(resultado_subcategorias)

fig = px.bar(
    resultado_categorias.reset_index(),
    x="Category",
    y="Profit",
    title="Ganancias totales por categoría",
    text_auto="$,.0f",
    labels={
    "Category": "Categoría",
    "Profit": "Ganancias ($)"
    }
)

st.plotly_chart(fig)

fig = px.bar(
    resultado_subcategorias.reset_index().sort_values(
        "Profit",
        ascending=True
    ),
    x="Profit",
    y="Sub-Category",
    orientation="h",
    title="Ganancias totales por subcategoría",
    text_auto="$,.0f",
    labels={
        "Sub-Category": "Subcategoría",
        "Profit": "Ganancias ($)"
    }
)

fig.update_traces(
    textposition="outside",
    cliponaxis=False
)

fig.update_xaxes(
    range=[-30000, 65000]
)

fig.update_layout(
    height=700,
    width=1100,
    margin=dict(r=120)
)

st.plotly_chart(fig)


print(resultado_categorias )

# print(resultado_subcategorias)

# print(resultado_productos)

# print(
#     resultado_productos.sort_values(
#         "Profit",
#         ascending=True
#     ).head(10)
# )

# print(resultado_productos_perdidas.sort_values("Profit", ascending=True))