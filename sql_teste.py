import sqlite3 as sql

# Conecte ao banco de dados (ou crie um novo se não existir)
conn = sql.connect('psi.db')
cursor = conn.cursor()

# Crie a tabela forecast
cursor.execute('''
CREATE TABLE forecast (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Material TEXT NOT NULL,
    ModelRep TEXT NOT NULL,
    FCST_Indireto_SP TEXT NOT NULL,
    FCST_POA TEXT NOT NULL,
    FCST_FLN TEXT NOT NULL,
    FCST_PE TEXT NOT NULL,
    Data_Referencia DATE NOT NULL,
    Data_FCST DATE NOT NULL
)
''')

# Salve (commit) as alterações
conn.commit()

# Feche a conexão
conn.close()
