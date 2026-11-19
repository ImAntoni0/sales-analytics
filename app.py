import pandas as pd

import streamlit as st

from analysis import (
    analizar_categorias, 
    analizar_subcategorias,
    analizar_productos, 
    analizar_productos_perdidas,
    analizar_descuentos, 
    analizar_perdidas_por_descuentos, 
    analizar_transacciones_perdida,
    analizar_rentabilidad_producto
)

from charts import (
    grafica_ganancias_categorias,
    grafica_ganancias_subcategorias,
    grafica_ganancias_descuentos
)

df = pd.read_excel("sample_superstore.xls")

resultado_categorias = analizar_categorias(df)

resultado_subcategorias = analizar_subcategorias(df)

resultado_productos = analizar_productos(df)

resultado_productos_perdidas = analizar_productos_perdidas(df)

resultado_descuentos = analizar_descuentos(df)

resultado_analizar_perdidas_por_descuentos = analizar_perdidas_por_descuentos(df)

resultado_analizar_transacciones_perdida = analizar_transacciones_perdida(df, "GBC Ibimaster 500 Manual ProClick Binding System",0.7)

resultado_analizar_transacciones_perdida["Cost"] = resultado_analizar_transacciones_perdida["Sales"] - resultado_analizar_transacciones_perdida["Profit"]

resultado_analizar_transacciones_perdida["Cost per Unit"] = (
    resultado_analizar_transacciones_perdida["Cost"] /
    resultado_analizar_transacciones_perdida["Quantity"]
)

resultado_analizar_transacciones_perdida["Original Price per Unit"] = (
    resultado_analizar_transacciones_perdida["Sales"] /
    (
        resultado_analizar_transacciones_perdida["Quantity"] *
        (1 - resultado_analizar_transacciones_perdida["Discount"])
    )
)

resultado_analizar_transacciones_perdida["Price After Discount"] = (
    resultado_analizar_transacciones_perdida["Original Price per Unit"] *
    (1 - resultado_analizar_transacciones_perdida["Discount"])
)

resultado_analizar_transacciones_perdida["Loss per Unit"] = (
    -resultado_analizar_transacciones_perdida["Profit"] /
    resultado_analizar_transacciones_perdida["Quantity"]
)

resultado_analizar_transacciones_perdida = (
    resultado_analizar_transacciones_perdida.round(2)
)


resultado_analizar_rentabilidad_producto = analizar_rentabilidad_producto(df,"GBC Ibimaster 500 Manual ProClick Binding System")

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

fig = grafica_ganancias_categorias(resultado_categorias)

st.plotly_chart(fig)

fig = grafica_ganancias_subcategorias(resultado_subcategorias)

st.plotly_chart(fig)

st.subheader("Análisis de productos con pérdidas")

st.dataframe(
    resultado_productos_perdidas.sort_values(
        "Profit",
        ascending=True
    )
)

st.subheader("Análisis descuentos")

st.dataframe(resultado_descuentos)

fig = grafica_ganancias_descuentos(resultado_descuentos)

st.plotly_chart(fig)

st.subheader("Análisis descuentos con perdidas")

st.dataframe(resultado_analizar_perdidas_por_descuentos)

st.subheader("Analisis de descuento con perdidas del 70%")

st.dataframe(resultado_analizar_transacciones_perdida)

st.subheader("Análisis de descuento de producto: ")

st.dataframe(resultado_analizar_rentabilidad_producto)

# print(resultado_categorias )

# print(resultado_subcategorias)

# print(resultado_productos)

# print(
#     resultado_productos.sort_values(
#         "Profit",
#         ascending=True
#     ).head(10)
# )

# print(resultado_productos_perdidas.sort_values("Profit", ascending=True))