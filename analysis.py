
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

