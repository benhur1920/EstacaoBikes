import pandas as pd
import unidecode
import re

def carregando_a_url():
    url =  'http://dados.recife.pe.gov.br/it/dataset/7fac73fa-c0bb-4bae-9c21-2a45b82016a2/resource/e6e4ac72-ff15-4c5a-b149-a1943386c031/download/estacoesbike.csv'
    df = pd.read_csv(url, sep=';', encoding='utf-8')
    return df
    
def Aplicando_a_filtragem_retirar_bairros_fora_do_recife(df):
    df = df.query("bairro != 'Prazeres' and bairro != 'Piedade' and bairro != 'Bairro Novo' and bairro != 'Casa Caiada' and bairro != 'Carmo' and bairro != 'Varadouro' ")
    return df

def aplicando_capitalize_no_df(df):
    df.columns = df.columns.str.capitalize()
    return df

def criando_coluna_Regiao(df):
    dicionario = {
        'Centro': [
            'Boa Vista', 'Cabanga', 'Coelhos', 'Ilha Do Leite', 'Ilha Joana Bezerra',
            'Paissandu', 'Recife', 'Santo Amaro', 'Santo Antônio', 'Soledade', 'São José'
        ],
        'Noroeste': [
            'Aflitos', 'Alto Do Mandu', 'Alto José Bonifácio', 'Alto José Do Pinho', 'Apipucos',
            'Brejo Da Guabiraba', 'Brejo De Beberibe', 'Casa Amarela', 'Casa Forte',
            'Córrego Do Jenipapo', 'Derby', 'Dois Irmãos', 'Espinheiro', 'Graças', 'Guabiraba',
            'Jaqueira', 'Macaxeira', 'Mangabeira', 'Monteiro', 'Morro Da Conceição',
            'Nova Descoberta', 'Parnamirim', 'Passarinho', 'Pau Ferro', 'Poço', 'Santana',
            'Sítio Dos Pintos', 'Tamarineira', 'Vasco Da Gama'
        ],
        'Norte': [
            'Alto Santa Terezinha', 'Arruda', 'Beberibe', 'Bomba Do Hemetério', 'Cajueiro',
            'Campina Do Barreto', 'Campo Grande', 'Dois Unidos', 'Encruzilhada', 'Fundão',
            'Hipódromo', 'Linha Do Tiro', 'Peixinhos', 'Ponto De Parada', 'Porto Da Madeira',
            'Rosarinho', 'Torreão', 'Água Fria'
        ],
        'Oeste': [
            'Caxangá', 'Cidade Universitária', 'Cordeiro', 'Engenho Do Meio',
            'Ilha Do Retiro', 'Iputinga', 'Madalena', 'Prado', 'Torre',
            'Torrões', 'Várzea', 'Zumbi'
        ],
        'Sudeste': [
            'Afogados', 'Areias', 'Barro', 'Bongi', 'Caçote', 'Coqueiral', 'Curado',
            'Estância', 'Jardim São Paulo', 'Jiquiá', 'Mangueira', 'Mustardinha',
            'San Martin', 'Sancho', 'Tejipió', 'Totó'
        ],
        'Sul': [
            'Boa Viagem', 'Brasília Teimosa', 'Cohab', 'Ibura',
            'Imbiribeira', 'Ipsep', 'Jordão', 'Pina'
        ]
    }

    # Criar dicionário com bairros sem acento como chave
    bairro_para_regiao = {
        unidecode.unidecode(bairro).strip().title(): regiao
        for regiao, bairros in dicionario.items()
        for bairro in bairros
    }

    # Normalizar a coluna 'Bairro' (sem acento e formatado corretamente)
    df['Bairro_norm'] = df['Bairro'].astype(str).apply(lambda x: unidecode.unidecode(x).strip().title())

    # Criar a coluna Região
    df['Região'] = df['Bairro_norm'].map(bairro_para_regiao)

    # (Opcional) remover a coluna auxiliar
    df.drop(columns='Bairro_norm', inplace=True)

    return df

def tratando_colunas_de_coordeandas(df):
    # Convertendo para float, ignorando erros (caso tenha valores não numéricos)
    df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')
    df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
    return df



def remover_ate_primeira_consoante(nome):
    if pd.isnull(nome):
        return nome
    match = re.search(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', nome)
    if match:
        return nome[match.start():]
    else:
        return nome  # Se não tiver consoante, retorna o nome original

def aplicar_remocao_no_df(df):
    df['Nome'] = df['Nome'].apply(remover_ate_primeira_consoante)
    return df


def main():
    # Carregando os dataframes
    df = carregando_a_url()
    df = Aplicando_a_filtragem_retirar_bairros_fora_do_recife(df)
    df = aplicando_capitalize_no_df(df)
    df = criando_coluna_Regiao(df)
    df = tratando_colunas_de_coordeandas(df)
    df = aplicar_remocao_no_df(df)

    return df

# criar a variavel df com o dataframe
df = main()

# Definição do programa principal será o main()
if __name__ == '__main__':
    print("Executando estacaoBike.py diretamente")
    
    

