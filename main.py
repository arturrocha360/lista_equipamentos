
import pandas as pd
import os

# Substitua 'caminho/para/seu/arquivo.xlsx' pelo caminho do seu arquivo Excel
pasta = 'C:/Users/artur.rocha/Documents/Listas de Equipamento/listas equipamento'

# Lista para armazenar os DataFrames de cada arquivo
dfs = []

# Percorrer todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    # Verificar se o arquivo é um arquivo Excel
    if arquivo.endswith('.xlsx') or arquivo.endswith('.xls'):
        # Caminho completo do arquivo
        caminho_arquivo = os.path.join(pasta, arquivo)
        # Ler o arquivo Excel e armazenar o DataFrame na lista
        linha_inicial = 9
        coluna_final= 'N'
        df = pd.read_excel(caminho_arquivo,sheet_name='ListaEquipamentos', skiprows=linha_inicial-1)
        # Remova as colunas com cabeçalhos 'Unnamed'
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        # Remova as linhas que contêm apenas valores NaN em todas as colunas
        df = df.dropna(how='all')
        
        dfs.append(df)

# Concatenar todos os DataFrames em um único DataFrame
df_final = pd.concat(dfs, ignore_index=True)

caminho_arquivo_excel = 'arquivo.xlsx'

df_final.to_excel(caminho_arquivo_excel, index=False)

print("Arquivo Excel criado e abastecido com sucesso!")
