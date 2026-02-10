import pandas as pd

def carregar_dados(caminho):
    df = pd.read_csv(caminho)
    return df

def tratar_dados(df):
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    df['faturamento'] = df['quantidade'] * df['preco_unitario']
    
    # Removendo registros inválidos
    df = df[df['quantidade'] > 0]
    df = df[df['preco_unitario'] > 0]
    
    return df

if __name__ == "__main__":
    df = carregar_dados("../data/vendas.csv")
    df_tratado = tratar_dados(df)
    print(df_tratado.head())
  
