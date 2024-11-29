import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('psi.db')
cursor = conn.cursor()

# Executar o comando para excluir as colunas
try:
    cursor.execute('''ALTER TABLE zmb51
                      DROP COLUMN data_total''')
    cursor.execute('''ALTER TABLE zmb51
                      DROP COLUMN 'data total' ''')
    conn.commit()
    print("Colunas excluídas com sucesso.")
except sqlite3.OperationalError as e:
    print(f"Erro ao excluir colunas: {e}")

# Fechar a conexão
conn.close()
