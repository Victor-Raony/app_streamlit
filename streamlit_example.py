# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:49:38 2022

@author: maria
"""

import pandas as pd
import streamlit as st
import numpy as np


col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

df = pd.read_csv('covid-variants.csv') 
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

paises = list(df['location'].unique())

variants = list(df['variant'].unique())

tipo = 'Casos diários'
titulo = tipo + ' para ' 


pais = st.sidebar.selectbox('Selecione o pais', ['Todos']+ paises)
variante = st.sidebar.selectbox('Selecione a variante', ['Todas'] + variants )

color = st.sidebar.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)
start_color, end_color = st.sidebar.select_slider(
     'Select a range of color wavelength',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
     value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

def load_data():
    data = pd.read_csv('covid-variants.csv') 

    return data


def convert_df(df):
  
    return df.to_csv().encode('utf-8')

my_large_df = load_data()
csv = convert_df(my_large_df)

st.sidebar.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )



if(pais !=  'Todos'):
    st.header('Mostrando dados para ' + pais)
    df = df[df['location'] == pais]
    titulo = titulo + pais
else:
    st.header('Mostrando dados para todos os países')

if(variante !=  'Todas'):
    st.text('Mostrando dados para a variante ' + variante)
    df = df[df['variant'] == variante]
    titulo = titulo + ' (variante : ' + variante + ')' 
else:
    st.text('Mostrando dados para todas as variantes')
    titulo = titulo + '(todas as variantes)'
    

dfShow   = df.groupby(by=["date"]).sum()

import plotly.express as px

fig = px.bar(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title=titulo )
st.plotly_chart(fig, use_container_width=True)

fig = px.bar(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title=titulo )
st.plotly_chart(fig, use_container_width=True)


