import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write('Hello world')

st.title("Titulo")
st.markdown('##Titulo Markdown')
st.subheader("Clase 9 - M5")
st.subheader("Clase 10 - M6")
st.write("hola, hola")
st.write("***")
st.markdown('[Google](https://www.google.com.pe)')

df = pd.read_csv('hola.csv')
df.dropna(inplace=True)

st.title("Exploracion de vinos")
if st.checkbox('Mostrar nombre del boton'):
    st.dataframe(df)

if st.checkbox('Lista de datos'):
    if st.button("Mostrar head"):
        st.dataframe(df.head(5))
    if st.button("Mostrar describe"):
        st.dataframe(df.describe())

st.subheader("Informacion de dimensiones")
df_dim = st.radio("Dimension a mostrar:",('Filas','Columnas'), horizontal =True)
if df_dim == 'Columnas':
    st.write(df.columns)
if df_dim == 'Filas':
    st.write(df.shape[0])

if st.checkbox("Mostrar la visualizacion"):
    fig = plt.figure()
    sns.histplot(data=df,x="points", bins= 10)
    st.pyplot(fig)