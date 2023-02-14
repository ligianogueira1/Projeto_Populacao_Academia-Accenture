# Ynna é uma empresária que precisa saber a população total de um país separada por estados (pode-se escolher a quantidade de registros), além de também precisar saber qual é a média
# de renda desta população. Sendo assim, é necessário a criação de dois csv's:
# 1) Contendo as informações dos paises e população com estado;
# 2) Contendo a média salarial da população.
# Crie uma maquina virtual com o nome "exercicio-etl-ynna" e execute o programa em Python para ler os arquivos gerados.
# Crie uma relação entre estes arquivos (JOIN - no pandas) e importe estes dados para uma tabela no SQL Server.

# ==== Resolução =====

# Passo 1: criação do arquivo populacao.csv para armazenar a população total do estado e o país no qual está contido.
# Passo 2: criação do arquivo renda_media.csv para armazenar a renda média da população de cada estado.
# Passo 3: importação da biblioteca pandas para leitura e exibição dos arquivos.

import pandas as pd
import pyodbc

populacao = pd.read_csv("populacao.csv")
renda_media = pd.read_csv("renda_media.csv")

print("Ynna, esta é a lista da população total de cada estado e o país ao qual pertence: ")
print("-" * 150)
print(populacao)
print("-" * 150)
print(" " * 150)

print("Agora, veja a média salarial de cada população: ")
print("-" * 150)
print(renda_media)
print("-" * 150)
print(" " * 150)

relatorio = pd.merge(populacao, renda_media, on="id")
print("E aqui está o relatório com todas as informações anteriores, contendo estado, país, população e média de renda: ")
print("-" * 150)
print(relatorio)
print("-" * 150)


# Passo 4: Criando uma conexão com o SQL Server
conn = pyodbc.connect("Driver={ODBC Driver 18 for SQL Server};Server=tcp:exercicio-etl.database.windows.net,1433;Database=exercicio_etl_ynna;Uid=maquina_key;Pwd={Dezembro/9};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")


# Loop através de cada linha no DataFrame
for index, row in relatorio.iterrows():
    # Inserindo uma linha na tabela
    conn.execute("INSERT INTO relatorio (id, estado, país, população, renda_média) VALUES (?, ?, ?, ?, ?)", row[0], row[1], row[2], row[3], row [4])

# Salvando as mudanças
conn.commit()

# Fechando a conexão
conn.close()