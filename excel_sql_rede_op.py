import pandas as pd
import sqlite3


arquivo = 'Rede Operacional L89_R02.xlsx'
df = pd.read_excel(arquivo)

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('Rede Operacional L89.db')
# Escrever o DataFrame para o banco de dados SQLite3
df.to_sql('tabela_ip', conexao, index=False, if_exists='replace')

# Fechar a conexão
conexao.close()

print(f"O banco de dados SQLite3 {arquivo} foi criado com sucesso.")