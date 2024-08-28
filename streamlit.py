import streamlit as st
import pandas as pd

import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Informativo",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="auto",
)

# Título del dashboard
st.title(":bar_chart: Dashboard Ventas")

# Cargar datos
df = pd.read_csv("./supermarket_sales_clean.csv")

# KPIs
total_ventas = df["total"].sum()
total_productos = df["quantity"].sum()

# Mostrar KPIs
col1, col2 = st.columns(2)
col1.metric("Total Ventas", f"${total_ventas:,.2f}")
col2.metric("Total Productos", total_productos)


# Mostrar tabla de datos

col1c, col2c = st.columns(2)
# Mostrar ventas por producto

ventas_por_producto = df.groupby("product line")["total"].sum().reset_index()
fig = px.bar(
    ventas_por_producto,
    y="product line",
    x="total",
    title="Ventas por Producto",
    orientation="h",
    color="product line",
    labels={"product line": "Producto", "total": "Total"},
)
col1c.plotly_chart(fig)

# Mostrar ventas por género

ventas_por_genero = df.groupby("gender")["total"].sum().reset_index()
fig = px.pie(
    ventas_por_genero,
    values="total",
    names="gender",
    title="Ventas por Género",
    hole=0.5,
)
col2c.plotly_chart(fig)

# Mostrar ventas por ciudad

ventas_por_ciudad = df.groupby("city")["total"].sum().reset_index()
fig = px.bar(
    ventas_por_ciudad,
    x="city",
    y="total",
    title="Ventas por Ciudad",
    color="city",
    labels={"city": "Ciudad", "total": "Total"},
)
st.plotly_chart(fig)

# Mostrar ventas por mes
ventas_por_mes = df.groupby("date")["total"].sum().reset_index()
fig = px.line(
    ventas_por_mes,
    x="date",
    y="total",
    title="Ventas por Mes",
    labels={"date": "Fecha", "total": "Total"},
)
st.plotly_chart(fig)
