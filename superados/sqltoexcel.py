import sqlite3
import pandas as pd

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('dados.db')

# Ler a tabela em um DataFrame
df = pd.read_sql_query("SELECT * FROM tabela_dados", conexao)

# Fechar a conexão
conexao.close()

# Escrever o DataFrame para um arquivo Excel
df.to_excel('dados.xlsx', index=False)

print("Arquivo Excel 'dados.xlsx' criado com sucesso.")