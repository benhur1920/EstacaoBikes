import streamlit as st
import os



def exibir_sobre(totalLinhas):

    # caminho do arquivo imagem
    imagem_path3 = os.path.join(os.path.dirname(__file__), '..', 'images', 'estacaobike.jpg')  # ou o nome 
    
    col1, col2 = st.columns([3,4])  # proporção da largura das colunas

    with col1:
        st.image(imagem_path3, use_container_width=True,clamp=True, caption='Estação de bikes')  # define o tamanho da imagem em pixels
    with col2:
        
        st.markdown(
        f"""
        <div style="text-align: center;   margin-top: 10px">
        <h2>Principais centros de compras do Recife</h2>
            <p style="font-size: 20px;">
            Atualmente, a cidade do Recife conta com <strong> {totalLinhas} </strong> de estações de bicicletas públicas distribuídas em diversas regiões da capital. Essas estações fazem parte de um sistema de mobilidade urbana sustentável, que visa oferecer à população uma alternativa acessível, saudável e ambientalmente correta para seus deslocamentos diários.
            </p>
            <p style="font-size: 20px;">
            A disponibilização desse serviço pela Prefeitura do Recife é de extrema importância, especialmente em um contexto de grandes desafios urbanos, como congestionamentos, poluição do ar e altos custos com transporte individual. Além de estimular hábitos de vida mais saudáveis, o sistema de bicicletas compartilhadas contribui para a redução da emissão de gases poluentes e fortalece o conceito de cidades mais inclusivas e sustentáveis.
            </p>
            
        </div>
        """, unsafe_allow_html=True
    ) 
        
        

def mainSobre(totalLinhas):
    st.markdown("<hr style='border:2px'>", unsafe_allow_html=True)
    exibir_sobre(totalLinhas)
