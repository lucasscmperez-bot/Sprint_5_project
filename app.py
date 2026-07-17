import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análise de Anúncios de Vendas de Carros')
car_data = pd.read_csv('vehicles_us.csv')

# --- 1. Data Viewer ---
st.subheader('Data viewer')
show_data = st.checkbox('Mostrar todos os dados')
if show_data:
    st.dataframe(car_data)

# --- 2. Vehicle types by model ---
st.subheader('Tipos de veículos por modelo')
fig1 = px.bar(car_data, x="model", color="type")
st.plotly_chart(fig1, width='stretch')

# --- 3. Histogram of condition vs model_year ---
st.subheader('Histograma de condição vs ano do modelo')
fig2 = px.histogram(car_data, x="model_year", color="condition")
st.plotly_chart(fig2, width='stretch')

# --- 4. Compare price distribution ---
st.subheader('Comparar distribuição de preço entre modelos')
# Usando a coluna 'model' que existe no seu dataset
model_list = sorted(car_data['model'].unique())
model1 = st.selectbox('Selecione o modelo 1', model_list, index=0)
model2 = st.selectbox('Selecione o modelo 2', model_list, index=1)

normalize = st.checkbox('Normalizar histograma')
range_hist = None
if normalize:
    range_hist = 'percent'

# Filtrando pelos modelos selecionados
fig3 = px.histogram(car_data[car_data['model'].isin([model1, model2])], 
                    x="price", color="model", histnorm=range_hist)
st.plotly_chart(fig3, width='stretch')