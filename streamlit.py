import streamlit as st
import pandas as pd
import plotly.express as px

# mostrar ventas totales
# mostrar ventas por producto
# mostrar ventas por genero
# mostrar ventas por ciudad 



st.set_page_config(
    page_title='Dashboard Informativo', 
    page_icon=':bar_chart:', 
    layout='wide', 
    initial_sidebar_state='auto')
st.title(':bar_chart: Dashboard Ventas')

# Cargar datos
df = pd.read_csv('./supermarket_sales_clean.csv')

# kpi
total_ventas = int(df['total'].sum())
total_productos = df['quantity'].sum()

# crear columnas
col1, col2 = st.columns(2)

# mostrar kpi
with col1:
    st.metric('Total Ventas', f'${total_ventas:,.2f}')
    
with col2:
    st.metric('Total Productos', total_productos)


# mostrar ventas por producto
st.title('Ventas por Producto')
ventas_por_producto = df.groupby('product line')['total'].sum().reset_index()
ventar_por_genero = df.groupby("gender")["total"].sum().reset_index()
ventas_por_ciudad = df.groupby("city")["total"].sum().reset_index()


fig = px.bar(ventas_por_producto, 
             y='product line',
               x='total', 
               title='Ventas por Producto',
                 orientation="h",
                   color='product line')
st.plotly_chart(fig)

# # mostrar ventas por genero
# st.title('Ventas por Genero')
# fig = px.pie(ventar_por_genero, values='total',names=['Femenino','Masculino','Otros'], title='Ventas por Genero')
# st.plotly_chart(fig)

# # mostrar ventas por ciudad
# st.title('Ventas por Ciudad')
# fig = px.bar(ventas_por_ciudad, x='city', y='total', title='Ventas por Ciudad')
# st.plotly_chart(fig)


