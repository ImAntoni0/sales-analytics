
import pandas as pd


def analizar_categorias(df):

    categorias = df.groupby("Category").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Discount": "mean"
    })

    categorias["Profit Margin"] = (
        categorias["Profit"] / categorias["Sales"]
    ) * 100

    return categorias


def analizar_subcategorias(df):

    subcategorias = df.groupby("Sub-Category").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Discount": "mean"
    })

    subcategorias["Profit Margin"] = (
        subcategorias["Profit"] / subcategorias["Sales"]
    ) * 100

    return subcategorias


def analizar_productos(df):

    productos = df.groupby("Product Name").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum",
        "Discount": "mean"
    })

    productos["Profit Margin"] = (
        productos["Profit"] / productos["Sales"]
    ) * 100

    return productos


def analizar_productos_perdidas(df):

    productos = analizar_productos(df)

    productos_perdidas = productos[productos["Profit"] < 0]

    return productos_perdidas


def analizar_descuentos(df):

    descuentos = df.groupby("Discount").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    descuentos["Profit Margin"] = (
        descuentos["Profit"] / descuentos["Sales"]
    ) * 100

    descuentos["Loss Transactions"] = (
        df.groupby("Discount")["Profit"].apply(
            lambda x: (x < 0).sum()
        )
    )

    descuentos["Profitable Transactions"] = (
        df.groupby("Discount")["Profit"].apply(
            lambda x: (x > 0).sum()
        )
    )

    descuentos["Break-even Transactions"] = (
        df.groupby("Discount")["Profit"].apply(
            lambda x: (x == 0).sum()
        )
    )

    descuentos["Total Transactions"] = (
        descuentos["Loss Transactions"]
        + descuentos["Profitable Transactions"]
        + descuentos["Break-even Transactions"]
    )

    descuentos["Loss Transaction Rate"] = (
        descuentos["Loss Transactions"]
        / descuentos["Total Transactions"]
        * 100
    ).round(2)

    return descuentos


def analizar_perdidas_por_descuentos(df):

    perdidas = df[df["Profit"] < 0]

    descuento = perdidas.groupby("Discount").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    return descuento


def analizar_transacciones_producto_descuento(
    df, nombre_producto, descuento
):

    productos = df[
        (df["Discount"] == descuento) &
        (df["Product Name"] == nombre_producto)
    ]

    return productos


def analizar_costos_transacciones(transacciones):

    transacciones = transacciones.copy()

    transacciones["Cost"] = (
        transacciones["Sales"] - transacciones["Profit"]
    )

    transacciones["Cost per Unit"] = (
        transacciones["Cost"] / transacciones["Quantity"]
    )

    transacciones["Original Price per Unit"] = (
        transacciones["Sales"] /
        (
            transacciones["Quantity"] *
            (1 - transacciones["Discount"])
        )
    )

    transacciones["Price After Discount"] = (
        transacciones["Original Price per Unit"] *
        (1 - transacciones["Discount"])
    )

    transacciones["Profit per Unit"] = (
        transacciones["Profit"] / transacciones["Quantity"]
    )

    return transacciones.round(2)


def analizar_rentabilidad_producto(df, nombre_producto):

    producto = df[
        df["Product Name"] == nombre_producto
    ]

    producto_descuento = producto.groupby("Discount").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    producto_descuento["Profit Margin"] = (
        producto_descuento["Profit"] /
        producto_descuento["Sales"]
    ) * 100

    return producto_descuento


def indicadores_generales(df):

    resultado = df.agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    return resultado


def analizar_pedidos_por_descuento(df):


    detalle_pedidos_descuento = df.groupby(
        ["Order ID", "Discount"],
        as_index=False
    )["Profit"].sum()


    combinaciones_perdidas = detalle_pedidos_descuento[
        detalle_pedidos_descuento["Profit"] < 0
    ]

    combinaciones_rentables = detalle_pedidos_descuento[
        detalle_pedidos_descuento["Profit"] > 0
    ]

    combinaciones_equilibradas = detalle_pedidos_descuento[
        detalle_pedidos_descuento["Profit"] == 0
    ]


    resumen = pd.DataFrame(
        index=detalle_pedidos_descuento["Discount"].unique()
    )

    resumen.index.name = "Discount"


    resumen["Losses"] = (
        combinaciones_perdidas.groupby("Discount")["Profit"].sum()
    )

    resumen["Profits"] = (
        combinaciones_rentables.groupby("Discount")["Profit"].sum()
    )


    resumen["Loss Combinations"] = (
        combinaciones_perdidas.groupby("Discount").size()
    )

    resumen["Profitable Combinations"] = (
        combinaciones_rentables.groupby("Discount").size()
    )

    resumen["Break-even"] = (
        combinaciones_equilibradas.groupby("Discount").size()
    )

    resumen["Total Combinations"] = (
        detalle_pedidos_descuento.groupby("Discount").size()
    )

    resumen = resumen.fillna(0)


    resumen["Loss Rate"] = (
        resumen["Loss Combinations"]
        / resumen["Total Combinations"]
    ) * 100

    return resumen.sort_index()