
def analizar_categorias(df):
    # Analisis de rentabilidad por categoria
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

    return descuentos

def analizar_perdidas_por_descuentos(df):

    perdidas = df[df["Profit"] < 0]

    descuento = perdidas.groupby("Discount").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    })

    return descuento

def analizar_transacciones_perdida(df, nombre_producto, descuento):

    productos = df[
        (df["Profit"] < 0) & 
        (df["Discount"] == descuento) & 
        (df["Product Name"] == nombre_producto)
    ]

    return productos

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

# analizar_descuento_perdidas = resultado_descuentos[
#     resultado_descuentos["Profit"] < 0
# ]

# Cambio de prueba en desarrollo-dashboard

# Cambio exclusivo de nueva-funcionalidad