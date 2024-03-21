import sqlite3

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('dados.db')

# Cursor para executar comandos SQL
cursor = conexao.cursor()

# Consulta SQL para remover dados duplicados
consulta = """
           DELETE FROM tabela_dados
           WHERE rowid NOT IN (
               SELECT MIN(rowid)
               FROM tabela_dados
               GROUP BY Sistema, SUBSISTEMA, EQUIPAMENTO, FABRICANTE, MODELO, MEIO_FISICO, PROTOCOLO, DESCRIÇÃO
           )
           """

# Executar a consulta
cursor.execute(consulta)

# Commit para efetivar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()

print("Dados duplicados removidos com sucesso.")
