import streamlit as st
from utils.totalizadores import calcular_o_tamnnho_df, calular_a_quantidade_de_colunas
from dados.estacaoBike import df

def filtros_aplicados_nas_colunas(df):
    # Opções são os nomes das colunas
    opcoes_disponiveis = sorted(df.columns)

    # Multiselect para escolher as colunas
    filtro_opcao = st.multiselect('Selecione as colunas que deseja baixar', opcoes_disponiveis)

    # Se o usuário selecionar colunas
    if filtro_opcao:
        return df[filtro_opcao]
    else:
        # Se não selecionar nada, retorna o DataFrame original
        return df


def dataframe(df_filtrado):
    st.markdown("<hr>",
    unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="text-align: center;   margin-top: 60px">
            <h3>Download dos dados</h3>
                        
        </div>
        """, unsafe_allow_html=True
    )
    df_filtrao = df
    df_filtrado = filtros_aplicados_nas_colunas(df_filtrado)
    st.dataframe(df_filtrado)
    totalLinhas = calcular_o_tamnnho_df(df_filtrado)
    totalColunas =  calular_a_quantidade_de_colunas(df_filtrado)
    
    csv = df_filtrado.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')

    col1, col2, col3 =  st.columns([3,1,1])
   
    with col1:
        st.download_button(
            label="📥 Baixar CSV",
            data=csv,
            file_name='centros_comerciais_recife.csv',
            mime='text/csv'
        )
    with col2:
        st.metric(label="Total linhas do dataframe", value=totalLinhas, border=True)
    with col3:
        st.metric(label="Total colunas do dataframe", value=totalColunas, border=True)

def mainDataframe(df_filtrado):
    dataframe(df_filtrado)
