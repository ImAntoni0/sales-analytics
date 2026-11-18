# Sales Analytics Dashboard

## Descripción

Sales Analytics es un proyecto de análisis de datos y desarrollo de software que utiliza información de ventas para identificar patrones, evaluar la rentabilidad de los productos y detectar oportunidades de mejora en el rendimiento comercial.

El proyecto utiliza Python para procesar y analizar los datos, y Streamlit para desarrollar un dashboard interactivo que permita visualizar los resultados de manera sencilla.

## Tecnologías utilizadas

- **Python:** lenguaje principal de programación.
- **Pandas:** procesamiento y análisis de datos.
- **Streamlit:** desarrollo de nuestra aplicación web interactiva.
- **Plotly:** creación de gráficas y visualizaciones interactivas.
- **Git:** control de versiones.
- **GitHub:** almacenamiento y publicación del código fuente.
- **SQL / SQLite:** tecnologías previstas para trabajar con bases de datos.

## Objetivos del proyecto

- Analizar los datos de ventas para identificar patrones y tendencias comerciales.
- Evaluar la rentabilidad de las categorías, subcategorías y productos.
- Identificar productos que generan pérdidas y analizar los factores relacionados con ellas.
- Investigar cómo los descuentos afectan las ganancias.
- Desarrollar un dashboard interactivo que permita visualizar los resultados y facilitar la interpretación de los datos.

## Análisis realizados

### Análisis de ventas y rentabilidad

- Análisis de ventas, ganancias y unidades vendidas por categoría.
- Evaluación de la rentabilidad por subcategoría.
- Identificación de productos que generan pérdidas.
- Análisis de la relación entre descuentos y rentabilidad.

### Investigación de productos con pérdidas

Se realizó una investigación específica del producto GBC Ibimaster 500 Manual ProClick Binding System para comprender cómo los descuentos elevados afectan su rentabilidad.

Entre los resultados obtenidos se identificó que:

- El costo estimado por unidad es de $380.49.
- El precio original estimado por unidad es de $760.98.
- El precio despues del descuento por unidad es de $228.29.
- Con un descuento del 70%, el producto genera una pérdida aproximada de $152.20 por unidad.
- Las transacciones analizadas con un descuento del 70% acumulan una pérdida de aproximadamente $3,957.10.

## Estructura del proyecto

- `analysis.py`: contiene las funciones utilizadas para analizar los datos de ventas.
- `app.py`: contiene la aplicación web desarrollada con Streamlit.
- `main.py`: archivo principal utilizado durante las pruebas iniciales del proyecto.
- `requirements.txt`: contiene las dependencias necesarias para ejecutar el proyecto.
- `sample_superstore.xls`: conjunto de datos utilizado para realizar los análisis.
- `ventas.csv`: conjunto de datos utilizado durante las prácticas iniciales.
- `.gitignore`: especifica los archivos y carpetas que Git debe ignorar.
- `README.md`: documentación principal del proyecto.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ImAntoni0/sales-analytics.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd sales-analytics
```

### 3. Crear un entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar el dashboard

```bash
streamlit run app.py
```

## Funcionalidades del dashboard

### Indicadores generales

- Visualización de las ventas totales.
- Consulta de las ganancias totales.
- Seguimiento de las unidades vendidas.

### Análisis por categorías y subcategorías

- Comparación de ventas y ganancias entre categorías.
- Evaluación de la rentabilidad por subcategoría.
- Visualización de los resultados mediante gráficas interactivas.

### Análisis de productos

- Identificación de productos que generan pérdidas.
- Investigación de la rentabilidad de productos específicos.
- Análisis del impacto de los descuentos sobre las ganancias.

## Fuente de datos

El proyecto utiliza el conjunto de datos `sample_superstore.xls`, que contiene información relacionada con las ventas de productos.

Entre los datos disponibles se encuentran:

- Información de los pedidos.
- Categorías y subcategorías de productos.
- Nombres de los productos.
- Ventas y cantidades vendidas.
- Descuentos aplicados.
- Ganancias obtenidas.

Este conjunto de datos permite analizar el rendimiento comercial, evaluar la rentabilidad e investigar las pérdidas generadas por determinados productos.

## Estado del proyecto

El proyecto se encuentra actualmente en desarrollo.

### Completado

- Configuración del entorno de desarrollo.
- Análisis exploratorio de los datos de ventas.
- Funciones para analizar categorías, subcategorías y productos.
- Identificación e investigación de productos con pérdidas.
- Análisis del impacto de los descuentos en la rentabilidad.
- Desarrollo inicial del dashboard interactivo con Streamlit.
- Control de versiones mediante Git y GitHub.

### Próximas mejoras

- Mejorar el diseño y la organización del dashboard.
- Incorporar nuevas gráficas y visualizaciones interactivas.
- Ampliar el análisis de productos con pérdidas.
- Implementar una base de datos utilizando SQL o SQLite.
- Mejorar la estructura y organización del código.