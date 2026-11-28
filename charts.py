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
            "#0F766E" if valor >= 0 else "#C0392B"
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
            "#0F766E" if valor >= 0 else "#C0392B"
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

    df = resultado_descuentos.reset_index().copy()

    df["Discount"] = df["Discount"].map(
        lambda x: f"{x:.0%}"
    )

    df["Resultado"] = df["Profit"].apply(
        lambda x: "Pérdidas" if x < 0 else "Ganancias"
    )

    fig = px.bar(
        df,
        x="Profit",
        y="Discount",
        orientation="h",
        title="Ganancias según el nivel de descuento",
        text_auto="$,.0f",
        labels={
            "Discount": "Descuento",
            "Profit": "Ganancias ($)",
            "Resultado": "Resultado"
        },
        color="Resultado",
        color_discrete_map={
            "Ganancias": "#0F766E",
            "Pérdidas": "#C0392B"
        }
    )

    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        height=600,
        bargap=0.25,
        margin=dict(l=80, r=120, t=80, b=60),
        font=dict(size=14)
    )

    fig.update_yaxes(
        type="category",
        tickmode="array",
        tickvals=df["Discount"].tolist(),
        ticktext=df["Discount"].tolist(),
        title="Descuento (%)"
    )

    return fig



def grafica_precios_producto(valores_grafica):

    fig = px.bar(
        valores_grafica,
        x="Concepto",
        y="Precio",
        title="Comparación de precios por unidad",
        color_discrete_sequence=["#0F766E"]
    )

    return fig

def grafica_porcentaje_perdidas_descuentos(df):

    df = df.reset_index().copy()

    df["Discount"] = df["Discount"] * 100

    fig = px.bar(
        df,
        x="Discount",
        y="Loss Transaction Rate",
        title="Porcentaje de registros con pérdidas por descuento",
        color_discrete_sequence=["#0F766E"]
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        height=500,
        bargap=0.25,
        margin=dict(l=80, r=120, t=80, b=60),
        font=dict(size=14)
    )

    fig.update_xaxes(
        type="category",
        ticksuffix="%",
        title="Descuento (%)"
    )

    fig.update_yaxes(
        ticksuffix="%",
        title="Registros con pérdidas (%)"
    )

    return fig


def grafica_tasa_perdidas_pedidos(df):

    df = df.reset_index().copy()

    df["Discount"] = df["Discount"] * 100

    fig = px.bar(
        df,
        x="Discount",
        y="Loss Rate",
        title="Tasa de pérdidas por descuento en pedidos",
        color_discrete_sequence=["#0F766E"]
    )

    fig.update_traces(
        texttemplate="%{y:.2f}%",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        height=500,
        bargap=0.25,
        margin=dict(l=80, r=120, t=80, b=60),
        font=dict(size=14)
    )

    fig.update_xaxes(
        type="category",
        ticksuffix="%",
        title="Descuento (%)"
    )

    fig.update_yaxes(
        ticksuffix="%",
        title="Tasa de pérdidas (%)"
    )

    return fig

def grafica_perdidas_pedidos(df):

    df = df.reset_index().copy()

    df["Losses"] = df["Losses"].abs()

    df["Discount"] = (
        df["Discount"] * 100
    ).map(lambda x: f"{x:g}%")

    df = df.sort_values(
        by="Losses",
        ascending=True
    )

    fig = px.bar(
        df,
        x="Losses",
        y="Discount",
        orientation="h",
        title="Pérdidas acumuladas por descuento",
        labels={
            "Discount": "Descuento (%)",
            "Losses": "Pérdidas ($)"
        },
        color_discrete_sequence=["#0F766E"]
    )

    fig.update_xaxes(tickprefix="$")

    fig.update_traces(
        texttemplate="$%{x:,.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=600,
        bargap=0.25,
        margin=dict(l=80, r=120, t=80, b=60)
    )

    fig.update_yaxes(
        type="category",
        tickmode="array",
        tickvals=df["Discount"].tolist(),
        ticktext=df["Discount"].tolist()
    )

    return fig

def grafica_ganancias_pedidos(df):

    df = df.reset_index().copy()

    df = df.sort_values(
        by="Profits",
        ascending=True
    )

    df["Discount"] = (
        df["Discount"] * 100
    ).map(lambda x: f"{x:g}%")

    fig = px.bar(
        df,
        x="Profits",
        y="Discount",
        orientation="h",
        title="Ganancias acumuladas por descuento",
        labels={
            "Discount": "Descuento (%)",
            "Profits": "Ganancias ($)"
        },
        color_discrete_sequence=["#0F766E"]
    )

    fig.update_xaxes(tickprefix="$")

    fig.update_traces(
        texttemplate="$%{x:,.2f}",
        textposition="outside"
    )

    fig.update_layout(
        height=600,
        bargap=0.25,
        margin=dict(l=80, r=120, t=80, b=60)
    )

    fig.update_yaxes(
        type="category",
        tickmode="array",
        tickvals=df["Discount"].tolist(),
        ticktext=df["Discount"].tolist()
    )

    return fig


def grafica_combinaciones_por_resultado(df):

    df = df.reset_index().copy()

    df["Discount"] = (
        df["Discount"] * 100
    ).map(lambda x: f"{x:g}%")

    columnas = [
        "Loss Combinations",
        "Profitable Combinations",
        "Break-even"
    ]

    for columna in columnas:
        df[columna] = (
            df[columna] / df["Total Combinations"]
        ) * 100

    fig = px.bar(
        df,
        x="Discount",
        y=columnas,
        barmode="stack",
        title="Distribución porcentual de combinaciones por descuento",
        labels={
            "Discount": "Descuento (%)",
            "value": "Porcentaje de combinaciones",
            "variable": "Resultado"
        },
        color_discrete_map={
            "Loss Combinations": "#0F766E",
            "Profitable Combinations": "#0CC4B5",
            "Break-even": "#C0392B"
        }
    )

    fig.update_layout(
        barmode="stack",
        yaxis_title="Porcentaje (%)"
    )

    fig.update_yaxes(
        range=[0, 100],
        ticksuffix="%"
    )

    fig.update_xaxes(
        type="category",
        tickmode="array",
        tickvals=df["Discount"].tolist(),
        ticktext=df["Discount"].tolist()
    )

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
        text="Loss",
        color_discrete_sequence=["#C0392B"]
    )

    fig.update_xaxes(
        type="category",
        categoryorder="array",
        categoryarray=df["Discount"].tolist(),
        title="Descuento (%)"
    )

    fig.update_traces(
        texttemplate="$%{y:,.2f}",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        height=550,
        bargap=0.25,
        margin=dict(l=60, r=80, t=60, b=50),
        font=dict(size=12),
        yaxis_title="Pérdida económica ($)"
    )

    return fig


def grafica_top_productos_rentables(resultado_productos):

    productos = resultado_productos.reset_index().sort_values(
        "Profit",
        ascending=False
    ).head(10)

    fig = px.bar(
        productos,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top 10 productos más rentables",
        text_auto="$,.0f"
    )

    fig.update_traces(
        marker_color="#0F766E",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    return fig

def grafica_top_productos_perdidas(resultado_productos):

    productos = resultado_productos.reset_index().sort_values(
        "Profit",
        ascending=True
    ).head(10)

    fig = px.bar(
        productos,
        x="Profit",
        y="Product Name",
        orientation="h",
        title="Top 10 productos con mayores pérdidas",
        text_auto="$,.0f"
    )

    fig.update_traces(
        marker_color="#C0392B",
        textposition="outside",
        cliponaxis=False
    )

    fig.update_xaxes(
        autorange="reversed"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total descending"}
    )

    return fig