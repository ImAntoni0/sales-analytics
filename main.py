import pandas as pd

df = pd.read_excel("sample_superstore.xls")

# datos = {
#     "Producto": ["Laptop", "Mouse", "Laptop", "Teclado", "Mouse"],
#     "Mes": ["Octubre", "Octubre", "Octubre", "Septiembre", "Octubre"],
#     "Unidades": [2, 5, 1, 3, 10],
#     "Ingresos": [30000, 1250, 15000, 2250, 2500]
# }

# df = pd.DataFrame(datos)

# octubre = df[df["Mes"] == "Octubre"]

# Unidades = octubre.groupby("Producto")["Unidades"].sum()

# Ingresos = octubre.groupby("Producto")["Ingresos"].sum()

# resultado = Ingresos.sort_values(ascending=True)

# print(octubre)

# print(Unidades)

# print(Ingresos)

# print(resultado)


# df = pd.read_csv("ventas.csv")



# print(df)

# print(df.head())

# print(df.info())

# print(df.describe())

# df.loc[df["Producto"] == "Mouse" , "Ingresos"] = 5000

# df.loc[df["Producto"] == "Teclado" , "Ingresos"] = 3000

# print(df)

# df = df.drop_duplicates()

# print(df.duplicated())

# Comprobar valores faltantes
# print(df.isnull().sum())

# # Comprobar registros duplicados
# print(df.duplicated().sum())

# # print(df.describe())

# print(df["Sales"].describe())

# resultado = df.groupby("Product Name")["Sales"].sum()

# resultado = resultado.sort_values(ascending=False)

# print(resultado.head(10))

# resultado = df.groupby("Product Name")["Quantity"].sum()

# resultado = resultado.sort_values(ascending=False)

# print(resultado.head(10))

# Staples = df[df["Product Name"] == "Staples"]

# print(Staples["Sales"].sum())

# print(Staples["Quantity"].sum())

# resultado = df.groupby("Product Name").agg({
#     "Quantity": "mean",
#     "Sales": "sum"
# })

# resultado = resultado.sort_values("Sales", ascending=False)

# print(resultado.head(10))

# categorias = df.groupby("Category").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# # print(categorias)

# categorias["Profit Margin"] = (
#     categorias["Profit"] / categorias["Sales"]
# ) * 100

# print(categorias)



# resultado = furniture.groupby("Sub-Category").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado["Profit Margin"] = (resultado["Profit"] / resultado["Sales"]) * 100

# print(resultado.sort_values("Profit"))



# resultado_descuentos = furniture.groupby(
#     ["Sub-Category", "Discount"]
# ).agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum"
# })

# resultado_descuentos["Profit Margin"] = (
#     resultado_descuentos["Profit"] /
#     resultado_descuentos["Sales"]
# ) * 100

# print(resultado_descuentos)



# print(productos_perdida.sort_values("Profit"))



# print("Ganancias:", productos_ganancia["Profit"].sum())

# print("Pérdidas:", productos_perdida["Profit"].sum())

# print(productos_perdida.sort_values("Profit").head(5))

# print(
#     productos_perdida.sort_values("Profit Margin").head(5)
# )

# print(porcentaje_perdida)

# print("Profit total:", resultado_tables["Profit"].sum())

# print(productos_ganancia.sort_values("Profit",ascending=False))

# print("Productos con pérdidas:", len(productos_perdida))
# print("Productos con ganancias:", len(productos_ganancia))



# productos_perdida = resultado_tables[
#     resultado_tables["Profit"] < 0
# ]

# productos_ganancia = resultado_tables[
#     resultado_tables["Profit"] > 0
# ]

# porcentaje_perdida = (
#     len(productos_perdida) / len(resultado_tables)
# ) * 100


# tables = furniture[furniture["Sub-Category"] == "Tables"]

# resultado_tables = tables.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_tables["Profit Margin"] = (
#     resultado_tables["Profit"] /
#     resultado_tables["Sales"]
# ) * 100

# descuentos_bajos = resultado_tables[
#     resultado_tables["Discount"] <= 0.20
# ]

# descuentos_altos = resultado_tables[
#     resultado_tables["Discount"] > 0.20
# ]

# print("Margen con descuentos bajos:",
#       descuentos_bajos["Profit Margin"].mean())

# print("Margen con descuentos altos:",
#       (descuentos_altos["Profit"].sum()/
#       descuentos_altos["Sales"].sum()) * 100
# ) 


# print("Profit total:",
#       resultado_bookcases["Profit"].sum())



# bookcases = furniture[
#     furniture["Sub-Category"] == "Bookcases"
# ]


# resultado_bookcases = bookcases.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })


# resultado_bookcases["Profit Margin"] = (
#     resultado_bookcases["Profit"] /
#     resultado_bookcases["Sales"]
# ) * 100

# productos_perdida_bookcases = resultado_bookcases[
#     resultado_bookcases["Profit"] < 0
# ]

# productos_ganancia_bookcases = resultado_bookcases[
#     resultado_bookcases["Profit"] > 0
# ]

# porcentaje_perdida_bookcases = (
#     len(productos_perdida_bookcases) /
#     len(resultado_bookcases)
# ) * 100


# print("Productos con pérdidas:", len(productos_perdida_bookcases))

# print("Productos con ganancias:", len(productos_ganancia_bookcases))

# print(resultado_bookcases.sort_values("Profit").head(5))


# print("Porcentaje de productos con pérdidas:",
#       porcentaje_perdida_bookcases)

# print("Ganancias:",
#       productos_ganancia_bookcases["Profit"].sum())

# print("Pérdidas:",
#       productos_perdida_bookcases["Profit"].sum())

# print("Profit total:",
#       resultado_bookcases["Profit"].sum())



# furnishing = furniture[
#     furniture["Sub-Category"] == "Furnishings"
# ]

# resultado_furnishing = furnishing.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_furnishing["Profit Margin"] = (
#     resultado_furnishing["Profit"] /
#     resultado_furnishing["Sales"]
# ) * 100



# productos_perdida_furnishing = resultado_furnishing[
#     resultado_furnishing["Profit"] < 0
# ]

# productos_ganancia_furnishing = resultado_furnishing[
#     resultado_furnishing["Profit"] > 0
# ]

# porcentaje_perdida_furnishing = (
#     len(productos_perdida_furnishing) /
#     len(resultado_furnishing)
# ) * 100

# print("Porcentaje de productos con pérdidas:",
#       porcentaje_perdida_furnishing)

# print("Ganancias:",
#       productos_ganancia_furnishing["Profit"].sum())

# print("Pérdidas:",
#       productos_perdida_furnishing["Profit"].sum())

# print("Profit total:",
#       resultado_furnishing["Profit"].sum())

# furniture = df[df["Category"] == "Furniture"]

# Chairs = furniture[
#     furniture["Sub-Category"] == "Chairs"
# ]

# resultado_Chairs = Chairs.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_Chairs["Profit Margin"] = (
#     resultado_Chairs["Profit"] /
#     resultado_Chairs["Sales"]
# ) * 100

# productos_perdida_Chairs = resultado_Chairs[
#     resultado_Chairs["Profit"] < 0
# ]

# productos_ganancia_Chairs = resultado_Chairs[
#     resultado_Chairs["Profit"] > 0
# ]

# porcentaje_perdida_Chairs = (
#     len(productos_perdida_Chairs) /
#     len(resultado_Chairs)
# ) * 100

# print("Porcentaje de productos con pérdidas:",
#       porcentaje_perdida_Chairs)

# print("Ganancias:",
#       productos_ganancia_Chairs["Profit"].sum())

# print("Pérdidas:",
#       productos_perdida_Chairs["Profit"].sum())

# print("Profit total:",
#       resultado_Chairs["Profit"].sum())

# furniture = df[df["Category"] == "Furniture"]


# Chairs = furniture[
#     furniture["Sub-Category"] == "Chairs"
# ]

# resultado_furniture = furniture.groupby("Sub-Category").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_furniture["Profit Margin"] = (
#     resultado_furniture["Profit"] /
#     resultado_furniture["Sales"]
# ) * 100

# print(resultado_furniture.sort_values("Profit", ascending=False))

# print(resultado_furniture)


# productos_perdida_Chairs = resultado_Chairs[
#     resultado_Chairs["Profit"] < 0
# ]

# productos_ganancia_Chairs = resultado_Chairs[
#     resultado_Chairs["Profit"] > 0
# ]

# porcentaje_perdida_Chairs = (
#     len(productos_perdida_Chairs) /
#     len(resultado_Chairs)
# ) * 100

# print("Porcentaje de productos con pérdidas:",
#       porcentaje_perdida_Chairs)

# print("Ganancias:",
#       productos_ganancia_Chairs["Profit"].sum())

# print("Pérdidas:",
#       productos_perdida_Chairs["Profit"].sum())

# print("Profit total:",
#       resultado_Chairs["Profit"].sum())


# resultado_office = office_supplies.groupby("Sub-Category").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_office["Profit Margin"] = (
#     resultado_office["Profit"] /
#     resultado_office["Sales"]
# ) * 100


# print(resultado_office.sort_values("Profit", ascending=False))

# resultado_furniture["Profit Margin"] = (
#     resultado_furniture["Profit"] /
#     resultado_furniture["Sales"]
# ) * 100

# print(resultado_furniture.sort_values("Profit", ascending=False))

# furniture = df[df["Category"] == "Furniture"]





#Vamos a crear una variable que contenga la categoria que queremos filtrar en este caso es Office Suplies

# office_supplies = df[df["Category"] == "Office Supplies"]

# #Habiendo filtrado la categoria sigue filtrar la subcategoria que es Supplies, asi como en Furniture estan Chairs Table etc, aqui esta Supplies, y lo guardamos en otra variable llamada supplies

# supplies = office_supplies[
#     office_supplies["Sub-Category"] == "Supplies"
# ]

# #Aqui vamos a nombre por nombre elegir lo que queremos ver, en este caso el total de ventas , unidades vendidas etc. guardamos en resultado supplies

# resultado_supplies = supplies.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# #creamos una nueva columna llamada Profit Margin, en el que sacamos el margen de ganancia porcentual.

# resultado_supplies["Profit Margin"] = (
#     resultado_supplies["Profit"] /
#     resultado_supplies["Sales"]
# ) * 100

# ganancias_supplies = resultado_supplies[
#     resultado_supplies["Profit"] > 0
# ]

# perdidas_supplies = resultado_supplies[
#     resultado_supplies["Profit"] < 0
# ]

# porcentaje_perdidas_supplies = (
#     len(perdidas_supplies) /
#     len(resultado_supplies)
# ) * 100


# #por ultimo lo imprimimos con el profit de menor a mayor.

# print(resultado_supplies.sort_values("Profit", ascending=False))

# print(ganancias_supplies["Profit"].sum())

# print(perdidas_supplies["Profit"].sum())

# print(porcentaje_perdidas_supplies)

# print(technology["Sub-Category"].unique())

# technology = df[df["Category"] == "Technology"]

# phones = technology[
#     technology["Sub-Category"] == "Phones"
# ]

# resultado_phone = phones.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_phone["Profit Margin"] = (
#     resultado_phone["Profit"] /
#     resultado_phone["Sales"]
# ) * 100

# ganancias_phone = resultado_phone[
#     resultado_phone["Profit"] > 0
# ]

# perdidas_phone = resultado_phone[
#     resultado_phone["Profit"] < 0
# ]

# porcentaje_perdidas_phone = (
#     len(perdidas_phone) /
#     len(resultado_phone)
# ) * 100


# print(resultado_phone["Profit"].sum())

# print(ganancias_phone["Profit"].sum())

# print(perdidas_phone["Profit"].sum())

# print(porcentaje_perdidas_phone)


# technology = df[df["Category"] == "Technology"]

# accessories = technology[
#     technology["Sub-Category"] == "Accessories"
# ]

# resultado_accessories = accessories.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_accessories["Profit Margin"] = (
#     resultado_accessories["Profit"] /
#     resultado_accessories["Sales"]
# ) * 100

# ganancias_accessories = resultado_accessories[
#     resultado_accessories["Profit"] > 0
# ]

# perdidas_accessories = resultado_accessories[
#     resultado_accessories["Profit"] < 0
# ]

# porcentaje_perdidas_accessories = (
#     len(perdidas_accessories) /
#     len(resultado_accessories)
# ) * 100


# print(resultado_accessories["Profit"].sum())

# print(ganancias_accessories["Profit"].sum())

# print(perdidas_accessories["Profit"].sum())

# print(porcentaje_perdidas_accessories)

# print(technology["Sub-Category"].unique())


# technology = df[df["Category"] == "Technology"]

# machines = technology[
#     technology["Sub-Category"] == "Machines"
# ]

# resultado_machines = machines.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_machines["Profit Margin"] = (
#     resultado_machines["Profit"] /
#     resultado_machines["Sales"]
# ) * 100

# ganancias_machines = resultado_machines[
#     resultado_machines["Profit"] > 0
# ]

# perdidas_machines = resultado_machines[
#     resultado_machines["Profit"] < 0
# ]

# porcentaje_perdidas_machines = (
#     len(perdidas_machines) /
#     len(resultado_machines)
# ) * 100

# margen_descuentos = resultado_machines.groupby("Discount").agg({
#     "Profit Margin": ["mean", "count"],
#     "Profit": "sum"
# })



# print(margen_descuentos.sort_index())

# print(resultado_machines.sort_values("Profit", ascending=True))

# print(ganancias_machines["Profit"].sum())

# print(perdidas_machines["Profit"].sum())

# print(porcentaje_perdidas_machines)

# technology = df[df["Category"] == "Technology"]

# copiers = technology[
#     technology["Sub-Category"] == "Copiers"
# ]

# resultado_copiers = copiers.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_copiers["Profit Margin"] = (
#     resultado_copiers["Profit"] /
#     resultado_copiers["Sales"]
# ) * 100

# ganancias_copiers = resultado_copiers[
#     resultado_copiers["Profit"] > 0
# ]

# perdidas_copiers = resultado_copiers[
#     resultado_copiers["Profit"] < 0
# ]

# porcentaje_perdidas_copiers = (
#     len(perdidas_copiers) /
#     len(resultado_copiers)
# ) * 100

# print(resultado_copiers["Profit"].sum())

# print(ganancias_copiers["Profit"].sum())

# print(perdidas_copiers["Profit"].sum())

# print(porcentaje_perdidas_copiers)


# technology = df[df["Category"] == "Technology"]

# resultado_technologies = technology.groupby("Sub-Category").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_technologies["Profit Margin"] = (
#     resultado_technologies["Profit"] /
#     resultado_technologies["Sales"]
# ) * 100

# ganancias_technologies = resultado_technologies[
#     resultado_technologies["Profit"] > 0
# ]

# perdidas_technologies = resultado_technologies[
#     resultado_technologies["Profit"] < 0
# ]

# porcentaje_perdidas_technologies = (
#     len(perdidas_technologies) /
#     len(resultado_technologies)
# ) * 100




# print(resultado_technologies.sort_values("Profit", ascending=False))

# print(ganancias_technologies["Profit"].sum())

# print(perdidas_technologies["Profit"].sum())

# print(porcentaje_perdidas_technologies)

# print(technology["Category"].unique())



# technology = df[df["Category"] == "Technology"]

# machines = technology[
#     technology["Sub-Category"] == "Machines"
# ]

# resultado_machines = machines.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# resultado_machines["Profit Margin"] = (
#     resultado_machines["Profit"] /
#     resultado_machines["Sales"]
# ) * 100

# productos_perdidas_machines = resultado_machines[
#     resultado_machines["Profit"] < 0
# ]

# print(productos_perdidas_machines.sort_values(
#     "Profit", ascending=True
# ).head(5))


# productos_investigar = machines[
#     machines["Product Name"].isin([
#         "Cubify CubeX 3D Printer Double Head Print",
#         "Epson TM-T88V Direct Thermal Printer - Monochrome - Desktop"
#     ])
# ]

# print(productos_investigar[
#     ["Product Name", "Sales", "Profit", "Quantity", "Discount"]
# ])

# ventas_descuento_alto = machines[
#     machines["Discount"] >= 0.7
# ]

# print(ventas_descuento_alto[
#     ["Product Name", "Sales", "Profit", "Discount"]
# ].sort_values("Profit"))

# print(productos_investigar[
#     productos_investigar["Product Name"].str.contains("Epson")
# ][["Product Name", "Sales", "Profit", "Quantity", "Discount"]])

# print(productos_investigar[
#     productos_investigar["Product Name"].str.contains("Cubify")
# ][["Product Name", "Sales", "Profit", "Quantity", "Discount"]])


# ventas_50 = machines[machines["Discount"] == 0.5]

# ganancias_50 = ventas_50[ventas_50["Profit"] > 0]

# perdidas_50 = ventas_50[ventas_50["Profit"] < 0]


# print("Ventas con ganancias:", len(ganancias_50))
# print("Ventas con pérdidas:", len(perdidas_50))
# print("Ganancia total:", ganancias_50["Profit"].sum())
# print("Pérdida total:", perdidas_50["Profit"].sum())

# ventas_40 = machines[machines["Discount"] == 0.4]

# ganancias_40 = ventas_40[ventas_40["Profit"] > 0]

# perdidas_40 = ventas_40[ventas_40["Profit"] < 0]

# print("Ventas con ganancias:", len(ganancias_40))
# print("Ventas con pérdidas:", len(perdidas_40))
# print("Ganancia total:", ganancias_40["Profit"].sum())
# print("Pérdida total:", perdidas_40["Profit"].sum())

# ventas_30 = machines[machines["Discount"] == 0.3]

# ganancias_30 = ventas_30[ventas_30["Profit"] > 0]

# perdidas_30 = ventas_30[ventas_30["Profit"] < 0]

# print(perdidas_30[
#     ["Product Name", "Sales", "Profit", "Quantity", "Discount"]
# ])

# okidata = machines[
#     machines["Product Name"].str.contains(
#         "Okidata C610n Printer",
#         case=False,
#         na=False
#     )
# ]

# print(okidata[
#     ["Sales", "Profit", "Quantity", "Discount"]
# ])

# print("Ventas con ganancias:", len(ganancias_30))
# print("Ventas con pérdidas:", len(perdidas_30))
# print("Ganancia total:", ganancias_30["Profit"].sum())
# print("Pérdida total:", perdidas_30["Profit"].sum())

technology = df[df["Category"] == "Technology"]


machines = technology[
    technology["Sub-Category"] == "Machines"
]

# resultado_machines = machines.groupby("Product Name").agg({
#     "Sales": "sum",
#     "Profit": "sum",
#     "Quantity": "sum",
#     "Discount": "mean"
# })

# perdidas_machines = resultado_machines[
#     resultado_machines["Profit"] < 0
# ]

# perdidas_machines = perdidas_machines.sort_values(
#     "Profit", ascending=True
# )

# print(perdidas_machines.head(5))

# print(perdidas_machines.tail(5))

okidata_perdidas = machines[
    (machines["Product Name"].str.contains(
        "Okidata C610n Printer",
        case=False,
        na=False
    ))
    &
    (machines["Profit"] < 0)
]

print(okidata_perdidas[
    ["Sales", "Profit", "Quantity", "Discount"]
])