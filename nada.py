SCL = [
    ['SCL-REM-03\\PAC-01', 'SCL-REM-02\\EL-01', 'QDBI-CLP-01\\QDBI', 'SCL-REM-01\\CP-FF', 'SCL-REM-01\\CP-RP', 'SCL-REM-01\\CP-TF', 'SCL-REM-03\\PESS-01', 'SCL-REM-03\\PL-01', 'INV-01', 'MME-01', 'QGD-CLP-01'],
    ['Painel Carregador de Baterias. Monitorado na remota 03.', 'Elevador 01. Monitorado na remota de Adequações', 'CLP do Quadro de Distribuição Bombas de Incêndio. ', 'Relé Falta de Fase da Cabine Primária, monitorado pela REM-01.', 'Relé de Proteção do disjuntor da Cabine Primária, monitorado pela REM-01.', 'Relé de Temperatura do Transformador, monitorado pela REM-01.', 'Painel Essencial. Monitorado na remota 03.', 'Painel de Luz 01. Monitorado na remota 03.', 'Inversor da UPS.', 'Multimedidor do QGD', 'CLP do Quadro Geral de Distribuição.'],
    ['REMOTA 3', 'REMOTA 2', 'QDBI', 'REMOTA 1', 'REMOTA 1', 'REMOTA 1', 'REMOTA 3', 'REMOTA 3', '-', '-', 'QGD']
]

# Criar um dicionário onde as chaves são os elementos da linha 3 e os valores são lista de listas das outras linhas
classificacao = {}

for i in range(len(SCL[0])):
    chave = SCL[2][i]
    if chave not in classificacao:
        classificacao[chave] = [[], []]
    for j in range(len(SCL) - 1):
        classificacao[chave][j].append(SCL[j][i])

# Imprimir a classificação
print(classificacao)