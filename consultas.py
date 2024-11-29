import pandas as pd
import sqlite3

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('psi.db')

# Escrever a consulta SQL
query = "SELECT * FROM zmb51 WHERE MODELO = 'C450'"

# Executar a consulta e carregar os resultados em um DataFrame do pandas
df = pd.read_sql_query(query, conn)

# Fechar a conexão com o banco de dados
conn.close()

# Printar os dados
print(df)
