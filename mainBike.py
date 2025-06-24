import streamlit as st
import os

st.set_page_config(
    page_title="Estacao Bikes Recife",  # Título da aba do navegador
    page_icon="🚀",                     # Ícone da aba (favicon), opcional
    layout="wide"                      # Layout da página, opcional
)


from dados.estacaoBike import df

from streamlit_option_menu import option_menu
from utils import sobre, graficos, dataframe
from datetime import date
from utils.totalizadores import hoje

# Criando os estilos num arquivo css
def carregar_css():
    css_path = os.path.join(os.path.dirname(__file__), 'css', 'assets.css')
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# chamando a funcao para carregamento do CSS
carregar_css()


# Mostra a data mais recente, importar dos totalizadores.py
#st.write(f"📅 Última atualização dos dados: {ultima_data.strftime('%d/%m/%Y')}")

def titulo_pagina():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(
            "<h1>Estação de Bikes do Recife</h1>"
            "<p>Fonte: Dados abertos da Prefeitura do Recife</p>",
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
                """
                <div style="margin-top: 40px;">
                    <a href="https://dados.recife.pe.gov.br/" target="_blank" class="botao-link">
                        🔗 Acessar fonte dos dados
                    </a>
                </div>
                """, unsafe_allow_html=True
        )
        # Exibe a data no formato desejado
        st.write(f"📅 Dados atualizados em: {hoje.strftime('%d/%m/%Y')}")


def filtros_aplicados(df, nome_do_filtro):
    # Opções são os nomes das colunas
    opcoes_disponiveis = sorted(df[nome_do_filtro].dropna().unique())

    # Multiselect para escolher o filtro
    filtro_opcao = st.multiselect(f'Selecione {nome_do_filtro}', opcoes_disponiveis)

    # Se o usuário selecionar colunas
    if filtro_opcao:
        return df[df[nome_do_filtro].isin(filtro_opcao)]
    else:
        # Se não selecionar nada, retorna o DataFrame original
        return df



def criacao_navegacao_e_filtros():
    # Cópia do DataFrame original
    df_filtrado = df.copy()

    # Sidebar: Menu + Filtros
    with st.sidebar:
        # Menu de navegação
        selected = option_menu(
            menu_title="Conheça",
            options=["Sobre", "Dashboards", "Dataframe"],
            icons=["info-circle", "bar-chart", "table"],
            menu_icon="cast",  # Ícone do próprio menu
            default_index=0
        )

        # Título dos filtros
        st.markdown("<h1>Filtros</h1>", unsafe_allow_html=True)
        
        # Filtro de Zona
        df_filtrado = filtros_aplicados(df_filtrado, 'Região')
       
        # Filtro de Bairro
        df_filtrado = filtros_aplicados(df_filtrado, 'Bairro')

    #  Calcular o total de linhas filtradas
    totalLinhas = df_filtrado.shape[0]

    # Conteúdo principal
    if selected == "Sobre":
        totalLinhas = df_filtrado.shape[0]
        sobre.mainSobre(totalLinhas)
    elif selected == "Dashboards":
        graficos.mainGraficos(df_filtrado)
    else:
        dataframe.mainDataframe(df_filtrado)


def main():
    titulo_pagina()
    criacao_navegacao_e_filtros()
    

# Definição do programa principal será o main()
if __name__ == '__main__':
    main()