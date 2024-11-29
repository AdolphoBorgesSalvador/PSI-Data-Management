import pandas as pd
import sqlite3

Zmb51_Caminho =r'C:\Users\fsp_adolpho.salvador\Desktop\Konica Minolta\Desktop Cloud - Documentos\Desktop\Py\SQL\ZMB51 CONSUMOS.xlsx'

zmb51= pd.read_excel(Zmb51_Caminho,sheet_name='base mb51')

zmb51.columns

zmb51=zmb51.drop(columns=['similares?', 'Cat.','riso obso', 'Comments'])

conn = sqlite3.connect('psi.db')

zmb51.to_sql('zmb51', conn, if_exists='replace', index=False)

conn.close()

