import pandas as pd
import plotly_express as px
import streamlit as st
car_data = pd.read_csv('vehicles_us.csv')
st.header('Análisis de vehículos basándonos en su kilometraje')
check_histograma = st.checkbox('Generar histograma')
check_dispersion = st.checkbox('Generar gráfico de dispersión')
check_marca = st.checkbox('Generar histograma por tipo de vehiculo')
if check_histograma:
    st.write('Histograma de datos de venta de vehículos')
    fig = px.histogram(car_data, x = "odometer")
    st.plotly_chart(fig, use_container_width=True)
if check_dispersion:
    st.write('Precio de vehiculos con respecto a su kilometraje')
    fig = px.scatter(car_data, x = "odometer", y = "price")
    st.plotly_chart(fig, use_container_width=True)
if check_marca:
    st.write('Histograma de tipos de vehiculos')
    fig = px.histogram(car_data, x = "type")
    st.plotly_chart(fig, use_container_width=True)