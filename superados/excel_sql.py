import pandas as pd
import sqlite3


arquivo = 'dados_R01.xlsx'
df = pd.read_excel(arquivo)

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('dados.db')
# Escrever o DataFrame para o banco de dados SQLite3
df.to_sql('tabela_dados', conexao, index=False, if_exists='replace')

# Fechar a conexão
conexao.close()

print("O banco de dados SQLite3 'dados.db' foi criado com sucesso.")