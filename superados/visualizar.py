import sqlite3

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('dados.db')

# Cursor para executar comandos SQL
cursor = conexao.cursor()

# Consulta SQL para selecionar uma linha da tabela (pode ser qualquer consulta que selecione dados)
consulta = "SELECT * FROM tabela_dados LIMIT 1"

# Executar a consulta
cursor.execute(consulta)

# Obter os nomes das colunas
nomes_colunas = [descricao[0] for descricao in cursor.description]

# Exibir os nomes das colunas
print("Nomes das colunas:")
print(nomes_colunas)

# Fechar a conexão
conexao.close()
