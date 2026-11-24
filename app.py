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
    grafica_precios_producto,
    grafica_porcentaje_perdidas_descuentos,
    grafica_perdidas_economicas_descuentos
)

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

df = pd.read_excel("sample_superstore.xls")

resultado_categorias = analizar_categorias(df)

resultado_subcategorias = analizar_subcategorias(df)

resultado_productos = analizar_productos(df)

resultado_productos_perdidas = analizar_productos_perdidas(df)

resultado_descuentos = analizar_descuentos(df)

resultado_indicadores_generales = indicadores_generales(df)

st.title("Sales Analytics Dashboard")

st.caption("Exploración y análisis de datos de ventas")

pagina = st.sidebar.radio(
    "Navegación",
    [
        "Resumen general",
        "Análisis de productos",
        "Análisis de descuentos"
    ]
)

if pagina == "Resumen general":

    st.header("Resumen general")

    st.subheader("Indicadores generales")

    ventas_totales = resultado_indicadores_generales["Sales"]
    ganancias_totales = resultado_indicadores_generales["Profit"]
    unidades_totales = resultado_indicadores_generales["Quantity"]

    col1, col2, col3 = st.columns(
        3,
        gap="medium",
        vertical_alignment="center"
        )

    with col1:
        with st.container(border=True):
            st.caption("VENTAS TOTALES")
            st.markdown(
                f"<h2>${ventas_totales:,.2f}</h2>",
                unsafe_allow_html=True
            )
            st.caption("Importe total de ventas")

    with col2:
        with st.container(border=True):
            st.caption("GANANCIAS TOTALES")
            st.markdown(
                f"<h2 style='color: #6eaa5b;'>"
                f"${ganancias_totales:,.2f}</h2>",
                unsafe_allow_html=True
            )
            st.caption("Beneficio total obtenido")

    with col3:
        with st.container(border=True):
            st.caption("UNIDADES VENDIDAS")
            st.markdown(
                f"<h2>{unidades_totales:,.0f}</h2>",
                unsafe_allow_html=True
            )
            st.caption("Cantidad total de unidades")


    col1, col2 = st.columns([5, 6], gap="large")

    with col1:
        st.subheader("Análisis de rentabilidad por categoría")
        st.dataframe(
            resultado_categorias,
            column_config={
                "_index": st.column_config.TextColumn("Categoría"),
                "Sales": st.column_config.NumberColumn(
                    "Ventas",
                    format="$%,.2f"
                ),
                "Profit": st.column_config.NumberColumn(
                    "Ganancias",
                    format="$%,.2f"
                ),
                "Quantity": st.column_config.NumberColumn(
                    "Unidades",
                    format="%.0f"
                ),
                "Discount": st.column_config.NumberColumn(
                    "Descuento promedio",
                    format="percent"
                ),
                "Profit Margin": st.column_config.NumberColumn(
                    "Margen de ganancia",
                    format="%.2f%%"
                )
            },
            hide_index=False,
            width="stretch"
        )

    with col2:
        fig = grafica_ganancias_categorias(resultado_categorias)
        st.plotly_chart(fig, width="stretch")




    st.subheader("Análisis de rentabilidad por subcategoría")

    st.dataframe(
        resultado_subcategorias,
        column_config={
            "_index": st.column_config.TextColumn("Subcategoría"),
            "Sales": st.column_config.NumberColumn(
                "Ventas",
                format="$%,.2f"
            ),
            "Profit": st.column_config.NumberColumn(
                "Ganancias",
                format="$%,.2f"
            ),
            "Quantity": st.column_config.NumberColumn(
                "Unidades",
                format="%.0f"
            ),
            "Discount": st.column_config.NumberColumn(
                "Descuento promedio",
                format="percent"
            ),
            "Profit Margin": st.column_config.NumberColumn(
                "Margen de ganancia",
                format="%.2f%%"
            )
        },
        hide_index=False,
        width="stretch"
    )


    fig = grafica_ganancias_subcategorias(resultado_subcategorias)
    st.plotly_chart(fig, width="stretch")

    mayor_ganancia = resultado_subcategorias.loc[
        resultado_subcategorias["Profit"].idxmax()
    ]

    mayor_perdida = resultado_subcategorias.loc[
        resultado_subcategorias["Profit"].idxmin()
    ]


    st.subheader("Hallazgos principales")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.caption("SUBCATEGORÍA MÁS RENTABLE")

            st.markdown(f"### {mayor_ganancia.name}")

            st.markdown(
                f"<h2 style='color: #6eaa5b;'>"
                f"${mayor_ganancia['Profit']:,.2f}</h2>",
                unsafe_allow_html=True
            )

    with col2:
        with st.container(border=True):
            st.caption("SUBCATEGORÍA CON MAYORES PÉRDIDAS")

            st.markdown(f"### {mayor_perdida.name}")

            st.markdown(
                f"<h2 style='color: #c13e3e;'>"
                f"${mayor_perdida['Profit']:,.2f}</h2>",
                unsafe_allow_html=True
            )


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

    cantidad_total = resultado_analizar_transacciones["Quantity"].sum()

    precio_original_promedio = (
        resultado_analizar_transacciones["Original Price per Unit"]
        * resultado_analizar_transacciones["Quantity"]
    ).sum() / cantidad_total

    precio_descuento_promedio = (
        resultado_analizar_transacciones["Price After Discount"]
        * resultado_analizar_transacciones["Quantity"]
    ).sum() / cantidad_total

    costo_promedio = (
        resultado_analizar_transacciones["Cost per Unit"]
        * resultado_analizar_transacciones["Quantity"]
    ).sum() / cantidad_total

    valores_grafica = {
        "Concepto": [
            "Precio original",
            "Precio con descuento",
            "Costo por unidad"
        ],
        "Precio": [
            precio_original_promedio,
            precio_descuento_promedio,
            costo_promedio
        ]
    }

    fig = grafica_precios_producto(valores_grafica)
    st.plotly_chart(fig, width="stretch")

    st.subheader("Análisis de descuentos")
    st.dataframe(resultado_descuentos)

    st.subheader("Descuentos con mayor porcentaje de pérdidas")

    descuentos_problematicos = resultado_descuentos.sort_values(
        by="Loss Transaction Rate",
        ascending=False
    )

    st.dataframe(descuentos_problematicos)

    fig = grafica_porcentaje_perdidas_descuentos(resultado_descuentos)
    st.plotly_chart(fig, width="stretch")

    fig = grafica_perdidas_economicas_descuentos(resultado_descuentos)
    st.plotly_chart(fig, width="stretch")

    fig = grafica_ganancias_descuentos(resultado_descuentos)
    st.plotly_chart(fig, width="stretch")

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