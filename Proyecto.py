import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('C:/Users/gabri/OneDrive/TripleTen/Curso/Sprint 7/Proyecto_s7/Proyecto_s7/vehicles_us.csv')

# Encabezado de la app
st.header('Visualización interactiva de datos de industria automotriz')

# Botón para histograma
if st.button('Histograma de dist. de datos'):
    st.write('Creación de histograma')
    fig = px.histogram(car_data, x='price')
    st.plotly_chart(fig, use_container_width=True)

st.write("---")

# Botón para gráfico de dispersión
if st.button('Creación de Gráfico de Dispersión'):
    st.write('Creación de gráfico de dispersión')
    fig = px.scatter(car_data, x='price', y='model_year')
    st.plotly_chart(fig, use_container_width=True)

