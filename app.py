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
    grafica_perdidas_economicas_descuentos,
    grafica_top_productos_rentables,
    grafica_top_productos_perdidas
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

    productos_rentables = resultado_productos[
        resultado_productos["Profit"] > 0
    ]

    productos_no_rentables = resultado_productos[
        resultado_productos["Profit"] < 0
    ]

    productos_punto_equilibrio = resultado_productos[
        resultado_productos["Profit"] == 0
    ]


    cantidad_productos_rentables = len(productos_rentables)

    cantidad_productos_no_rentables = len(productos_no_rentables)

    cantidad_productos_punto_equilibrio = len(productos_punto_equilibrio)


    porcentaje_productos_rentables = (
        cantidad_productos_rentables / len(resultado_productos)
    ) * 100

    porcentaje_productos_no_rentables = (
        cantidad_productos_no_rentables / len(resultado_productos)
    ) * 100

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Productos rentables",
            value=cantidad_productos_rentables,
            delta=f"{porcentaje_productos_rentables:.1f}% del total"
        )

    with col2:
        st.metric(
            label="Productos no rentables",
            value=cantidad_productos_no_rentables,
            delta=f"{porcentaje_productos_no_rentables:.1f}% del total"
        )

    with col3:
        st.metric(
            label="Productos en punto de equilibrio",
            value=cantidad_productos_punto_equilibrio
        )


    productos_disponibles = resultado_productos.index.tolist()

    producto_seleccionado = st.selectbox(
        "Selecciona un producto",
        productos_disponibles
    )

    resultado_producto_seleccionado = resultado_productos.loc[
        producto_seleccionado
    ]


    st.subheader("Detalle del producto seleccionado")

    col1, col2, col3, col4, col5 = st.columns(5)

    profit = resultado_producto_seleccionado["Profit"]

    if profit > 0:
        color_profit = "#6eaa5b"
    elif profit < 0:
        color_profit = "#C0392B"
    else:
        color_profit = "#808080"

    with col1:
        st.metric(
            "Ventas",
            f"${resultado_producto_seleccionado['Sales']:,.2f}"
        )

    with col2:
        st.markdown(
            "<p style='margin-bottom: 0; font-weight: 600;'>Ganancias</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h2 style='color: {color_profit}; margin: -12px 0 0 0;'>"
            f"${profit:,.2f}</h2>",
            unsafe_allow_html=True
        )

    with col3:
        st.metric(
            "Unidades vendidas",
            f"{resultado_producto_seleccionado['Quantity']:,.0f}"
        )

    with col4:
        st.metric(
            "Descuento promedio",
            f"{resultado_producto_seleccionado['Discount']:.1%}"
        )

    with col5:
        st.metric(
            "Margen de ganancia",
            f"{resultado_producto_seleccionado['Profit Margin']:.2f}%"
        )

    transacciones_producto = df[df["Product Name"] == producto_seleccionado]

    transacciones_perdidas = transacciones_producto[
        transacciones_producto["Profit"] < 0
    ]

    cantidad_transacciones_perdidas = len(transacciones_perdidas)

    porcentaje_transacciones_perdidas = (
        cantidad_transacciones_perdidas / len(transacciones_producto)
    ) * 100

    columnas_transacciones = [
        "Order Date",
        "Order ID",
        "Customer Name",
        "Segment",
        "Region",
        "Sales",
        "Quantity",
        "Discount",
        "Profit"
    ]

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Transacciones con pérdidas",
            cantidad_transacciones_perdidas
        )

    with col2:
        st.metric(
            "Porcentaje de transacciones con pérdidas",
            f"{porcentaje_transacciones_perdidas:.2f}%"
        )

    st.subheader("Historial de transacciones")

    st.caption(
        f"Total de transacciones: {len(transacciones_producto)}"
    )

    transacciones_producto = transacciones_producto[columnas_transacciones]
    transacciones_producto = transacciones_producto.sort_values(
    by="Order Date",
    ascending=False
    )

    st.dataframe(
        transacciones_producto,
        column_config={
            "Order Date": st.column_config.DateColumn(
                "Fecha del pedido",
                format="DD/MM/YYYY"
            ),
            "Order ID": "ID del pedido",
            "Customer Name": "Cliente",
            "Segment": "Segmento",
            "Region": "Región",
            "Sales": st.column_config.NumberColumn(
                "Ventas",
                format="$%,.2f"
            ),
            "Quantity": st.column_config.NumberColumn(
                "Unidades",
                format="%,.0f"
            ),
            "Discount": st.column_config.NumberColumn(
                "Descuento",
                format="percent"
            ),
            "Profit": st.column_config.NumberColumn(
                "Ganancias",
                format="$%,.2f"
            )
        },
        hide_index=True,
        width="stretch"
    )



    st.subheader("Productos más rentables")

    st.dataframe(
        resultado_productos.sort_values(
            "Profit",
            ascending=False
        ).head(10),
        column_config={
            "_index": st.column_config.TextColumn("Producto"),
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
                format="%,.0f"
            ),
            "Discount": st.column_config.NumberColumn(
                "Descuento",
                format="percent"
            ),
            "Profit Margin": st.column_config.NumberColumn(
                "Margen de ganancia",
                format="%.2f%%"
            )
        }
    )

    fig = grafica_top_productos_rentables(resultado_productos)
    st.plotly_chart(fig, width="stretch")

    st.subheader("Productos con pérdidas")

    st.dataframe(
        resultado_productos_perdidas.sort_values(
            "Profit",
            ascending=True
        ).head(10),
        column_config={
            "_index": st.column_config.TextColumn("Producto"),
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
                format="%,.0f"
            ),
            "Discount": st.column_config.NumberColumn(
                "Descuento",
                format="percent"
            ),
            "Profit Margin": st.column_config.NumberColumn(
                "Margen de ganancia",
                format="%.2f%%"
            )
        }
    )

    fig = grafica_top_productos_perdidas(resultado_productos_perdidas)
    st.plotly_chart(fig, width="stretch")


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