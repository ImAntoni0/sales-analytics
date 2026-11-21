import plotly.express as px


def grafica_ganancias_categorias(resultado_categorias):

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

    return fig

def grafica_ganancias_subcategorias(resultado_subcategorias):

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

    return fig

def grafica_ganancias_descuentos(resultado_descuentos):
    
    fig = px.bar(
        resultado_descuentos.reset_index(),
        x="Profit",
        y="Discount",
        orientation="h",
        title="Ganancias según el nivel de descuento",
        text_auto="$,.0f",
        labels={
            "Discount": "Descuento",
            "Profit": "Ganancias ($)"
        }
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        bargap=0.08,
        height=700,
        font=dict(size=14)
    )

    return fig

def grafica_precios_producto(valores_grafica):

    fig = px.bar(
        valores_grafica,
        x="Concepto",
        y="Precio",
        title="Comparación de precios por unidad"
    )

    return fig
