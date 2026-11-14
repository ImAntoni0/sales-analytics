import pandas as pd

from analysis import analizar_categorias, analizar_subcategorias, analizar_productos, analizar_productos_perdidas

df = pd.read_excel("sample_superstore.xls")

resultado_categorias = analizar_categorias(df)

resultado_subcategorias = analizar_subcategorias(df)

resultado_productos = analizar_productos(df)

resultado_productos_perdidas = analizar_productos_perdidas(df)

# print(resultado_categorias )

# print(resultado_subcategorias)

# print(resultado_productos)

# print(
#     resultado_productos.sort_values(
#         "Profit",
#         ascending=True
#     ).head(10)
# )

print(resultado_productos_perdidas.sort_values("Profit", ascending=True))