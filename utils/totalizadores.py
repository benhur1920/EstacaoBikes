from dados.estacaoBike import df
import pandas as pd
import streamlit as st
import re
from datetime import date

# Data atual
hoje = date.today()


#Calculo da ultima e menor data do sistema
#ultima_data =  df['data'].max()
#primeira_data =  df['data'].min()

def calcular_o_tamnnho_df(df):
    return df.shape[0]    

def calular_a_quantidade_de_colunas(df):
    colunasDisponiveis = sorted(df.columns)
    return len(colunasDisponiveis)  





# criar o df para zonas e bairros
df_zona = df.groupby('Região')[['Bairro']].count().reset_index()
df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL').sort_values(by='TOTAL', ascending=False)
df_mapa = df[['Bairro', 'Latitude', 'Longitude' ]]

