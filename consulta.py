import sqlite3

def ip_consulta(estacao, Descricao_Sistema):
    # Conexão com o banco de dados SQLite3
    conexao = sqlite3.connect('Rede Operacional L89.db')

    # Cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Nome que você quer pesquisar

    #estacao = "Júlio Prestes" #escolha do usuário
   #Descricao_Sistema = "Scap" #vem pelos equipamentos que foram escolhidos


    # Consulta SQL com filtro pelo nome
    consulta = f"""
            SELECT *
            FROM tabela_ip
            WHERE Estação LIKE '%{estacao}%' AND
                Descrição_Sistema LIKE '%{Descricao_Sistema}%'   
                    
            """
    # Executar a consulta
    cursor.execute(consulta)

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Exibir os resultados
    

    # Fechar a conexão
    conexao.close()
    return resultados

print(ip_consulta('Amador Bueno',"SMM")[0])
    
    


