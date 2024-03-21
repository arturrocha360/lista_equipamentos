import sqlite3

# Conexão com o banco de dados SQLite3
conexao = sqlite3.connect('dados.db')

# Cursor para executar comandos SQL
cursor = conexao.cursor()

# Nome que você quer pesquisar
dado_procurado = "WEG"


# Consulta SQL com filtro pelo nome
consulta = f"""
           SELECT *
           FROM tabela_dados
           WHERE Sistema LIKE '%{dado_procurado}%' OR
            EQUIPAMENTO LIKE '%{dado_procurado}%'  OR 
            PROTOCOLO LIKE '%{dado_procurado}%'    OR 
            MODELO LIKE '%{dado_procurado}%'       OR
            FABRICANTE LIKE '%{dado_procurado}%'   OR
            MEIO_FISICO LIKE  '%{dado_procurado}%' OR
            DESCRIÇÃO  LIKE   '%{dado_procurado}%' OR
            SUBSISTEMA LIKE '%{dado_procurado}%'   OR
            Sistemas_Lista_de_Ips LIKE '%{dado_procurado}%'   OR
            Grupo_de_equipamentos_Lista_de_IP LIKE '%{dado_procurado}%'   
                  
           """
# Executar a consulta
cursor.execute(consulta)

# Recuperar os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão
conexao.close()