import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('psi.db')
cursor = conn.cursor()

try:
    # Consulta SQL com JOIN para relacionar as tabelas
    cursor.execute('''
        SELECT t1.*, t2.*
        FROM tabela1 t1
        INNER JOIN tabela2 t2 ON t1.data = t2.data AND t1.material = t2.material
    ''')

    # Recuperar os resultados da consulta
    resultados = cursor.fetchall()

    # Exibir os resultados
    for linha in resultados:
        print(linha)

except sqlite3.OperationalError as e:
    print(f"Erro ao executar consulta: {e}")

# Fechar a conexão
conn.close()
