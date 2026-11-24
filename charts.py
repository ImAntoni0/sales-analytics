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

    fig.update_traces(
        marker_color=[
            "#6eaa5b" if valor >= 0 else "#c13e3e"
            for valor in fig.data[0].y
        ],
        textposition="outside" 
    )

    fig.update_yaxes(
        tickprefix="$",
        tickformat=",.0f"
    )

    fig.update_layout(
        height=450
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
        marker_color=[
            "#6eaa5b" if valor >= 0 else "#c13e3e"
            for valor in fig.data[0].x
        ],
        textposition="outside",
        cliponaxis=False
    )

    fig.update_xaxes(
        tickprefix="$",
        tickformat=",.0f",
        zeroline=True
    )

    fig.update_layout(
        height=700,
        margin=dict(r=100)
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

def grafica_porcentaje_perdidas_descuentos(df):

    df = df.reset_index().copy()

    df["Discount"] = df["Discount"] * 100

    df = df.sort_values(
        by="Loss Transaction Rate",
        ascending=False
    )

    fig = px.bar(
        df,
        x="Discount",
        y="Loss Transaction Rate",
        title="Porcentaje de registros con pérdidas por descuento"
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside",
    )

    fig.update_xaxes(ticksuffix="%")
    fig.update_yaxes(ticksuffix="%")

    return fig




def grafica_perdidas_economicas_descuentos(df):

    df = df.reset_index().copy()

    df = df[df["Profit"] < 0]

    df = df.sort_values(
        by="Profit",
        ascending=True
    )

    df["Loss"] = df["Profit"].abs()

    df["Discount"] = (
        (df["Discount"] * 100).astype(int).astype(str) + "%"
    )

    fig = px.bar(
        df,
        x="Discount",
        y="Loss",
        title="Pérdidas económicas por nivel de descuento",
        labels={
            "Discount": "Nivel de descuento",
            "Loss": "Pérdida económica ($)"
        },
        text="Loss"
    )

    fig.update_xaxes(
        type="category",
        categoryorder="array",
        categoryarray=df["Discount"].tolist()
    )

    fig.update_traces(
        texttemplate="$%{y:,.2f}",
        textposition="outside"
    )

    fig.update_layout(
        yaxis_title="Pérdida económica ($)",
        xaxis_title="Descuento"
    )

    return fig
