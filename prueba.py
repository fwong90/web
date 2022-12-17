import streamlit as st #1.15.2
import pandas as pd #1.5.2
import matplotlib.pyplot as plt #3.5.2
import seaborn as sns  #0.11.2

st.write('Hello world')

st.title("Titulo")
st.markdown('##Titulo Markdown')
st.subheader("Clase 9 - M5")
st.subheader("Clase 10 - M6")
st.write("hola, hola")
st.write("***")
st.markdown('[Google](https://www.google.com.pe)')

df = pd.read_csv('https://raw.githubusercontent.com/fwong90/web/main/hola.csv')
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