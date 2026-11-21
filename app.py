import pandas as pd

import streamlit as st

from analysis import (
    analizar_categorias, 
    analizar_subcategorias,
    analizar_productos, 
    analizar_productos_perdidas,
    analizar_descuentos, 
    analizar_perdidas_por_descuentos, 
    analizar_transacciones_producto_descuento,
    analizar_costos_transacciones,
    indicadores_generales
)

from charts import (
    grafica_ganancias_categorias,
    grafica_ganancias_subcategorias,
    grafica_ganancias_descuentos,
    grafica_precios_producto
)

df = pd.read_excel("sample_superstore.xls")

resultado_categorias = analizar_categorias(df)

resultado_subcategorias = analizar_subcategorias(df)

resultado_productos = analizar_productos(df)

resultado_productos_perdidas = analizar_productos_perdidas(df)

resultado_descuentos = analizar_descuentos(df)

resultado_analizar_perdidas_por_descuentos = analizar_perdidas_por_descuentos(df)

resultado_indicadores_generales = indicadores_generales(df)

st.title("Sales Analytics Dashboard")

st.write("Exploración y análisis de datos de ventas")

pagina = st.sidebar.radio(
    "Navegación",
    [
        "Resumen general",
        "Análisis de productos",
        "Análisis de descuentos"
    ]
)

if pagina == "Resumen general":

    st.write("Estamos en el resumen general")

    st.subheader("Indicadores generales")

    ventas_totales = resultado_indicadores_generales["Sales"]

    ganancias_totales = resultado_indicadores_generales["Profit"]

    unidades_totales = resultado_indicadores_generales["Quantity"]

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

elif pagina == "Análisis de productos":

    st.write("Estamos en el análisis de productos")

    st.subheader("Productos más rentables")

    st.dataframe(
        resultado_productos.sort_values(
            "Profit",
            ascending=False
        )
    )

    st.subheader("Productos con pérdidas")

    st.dataframe(
        resultado_productos_perdidas.sort_values(
            "Profit",
            ascending=True
        )
    )


elif pagina == "Análisis de descuentos":

    st.write("Estamos en el análisis de descuentos")

    producto_seleccionado = st.selectbox(
        "Selecciona un producto",
        resultado_productos.index
    )

    descuentos_disponibles = sorted(
        df[df["Product Name"] == producto_seleccionado]["Discount"].unique()
    )

    descuento_seleccionado = st.selectbox(
        "Selecciona un descuento",
        descuentos_disponibles
    )

    resultado_analizar_transacciones = analizar_transacciones_producto_descuento(
        df,
        producto_seleccionado,
        descuento_seleccionado
    )

    resultado_analizar_transacciones = analizar_costos_transacciones(
        resultado_analizar_transacciones
    )

    transaccion = resultado_analizar_transacciones.iloc[0]

    valores_grafica = {
        "Concepto": [
            "Precio original",
            "Precio con descuento",
            "Costo por unidad"
        ],
        "Precio": [
            transaccion["Original Price per Unit"],
            transaccion["Price After Discount"],
            transaccion["Cost per Unit"]
        ]
    }

    fig = grafica_precios_producto(valores_grafica)
    st.plotly_chart(fig)

    st.subheader("Análisis de descuentos")
    st.dataframe(resultado_descuentos)

    fig = grafica_ganancias_descuentos(resultado_descuentos)
    st.plotly_chart(fig)

    st.subheader("Transacciones del producto y descuento seleccionados")
    st.dataframe(resultado_analizar_transacciones)

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