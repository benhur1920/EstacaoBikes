import matplotlib as pl
import plotly.express as px
import streamlit as st
from utils.totalizadores import df_bairro, df_zona, df_mapa
#from funcoes import df_bairro, df_zona, df_mapa



    
#Criando o gráfico de distribuicao por zona
def grafico_zona(df):
        df_agrupado = df.groupby('Região')[['Bairro']].count().reset_index()
        
        fig =  px.treemap(
            df_agrupado,
            path=['Região'],
            values='Bairro',
            color='Bairro',
            
        )
        fig.update_layout(
            title={
                'text': 'Estação de bikes por região da cidade',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    
                }
            }
        )
        return fig
    # gerar os graficos a partir do df filtrado

    
    # Criando o gráfico de distribuicao por bairro
def grafico_bairro(df):
        df_bairro = df.groupby('Bairro').size().reset_index(name='TOTAL')
        df_bairro = df_bairro.sort_values('TOTAL', ascending=False)

        fig1 =  px.bar(
            df_bairro,
            x='Bairro',
            y='TOTAL',
            
        )
        fig1.update_layout(
            title={
                'text': 'Estação de bikes por bairro',
                'x': 0.5,
                'xanchor': 'center',
                'font': {
                    'size': 22,
                    
                }
            }
        )
        return fig1


    # Criando o gráfico de distribuicao por mapa
def grafico_mapa(df):
    fig3 = px.scatter_mapbox(
        df,
        hover_name='Nome',
        hover_data={
            
            'Região': True,
            'Bairro': True,
            'Localizacao': True
        },
        lat='Latitude',
        lon='Longitude',
        color='Região',  # ← as cores agora representam os valores da coluna 'Opção'
        zoom=11,
        height=500
    )

    # Aumenta o tamanho das bolinhas
    fig3.update_traces(marker=dict(size=15))  # ajuste o valor conforme necessário

    fig3.update_layout(
        title={
            'text': 'Estação de bikes na cidade do Recife',
            'x': 0.5,
            'xanchor': 'center',
            'font': {
                'size': 22,
                
            }
        }
    )

    return fig3


def mainGraficos(df_filtrado):

    st.markdown("<hr>", unsafe_allow_html=True)

    figura_zona = grafico_zona(df_filtrado)
    figura_bairro = grafico_bairro(df_filtrado)
    fig_mapa = grafico_mapa(df_filtrado)
    
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(figura_zona, use_container_width=True ) #config={"displayModeBar": False})
    with col2:
        st.plotly_chart(figura_bairro, use_container_width=True, stack=False)
    

    st.markdown("<hr>", unsafe_allow_html=True)

    fig_mapa.update_layout(mapbox_style="open-street-map")
    fig_mapa.update_layout(margin={"r":0, "t":30, "l":0, "b":0})

    # Aplica a margem com a div
    st.markdown('<div class="grafico-com-margem">', unsafe_allow_html=True)
    st.plotly_chart(fig_mapa, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)