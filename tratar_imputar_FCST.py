import pandas as pd
import sqlite3

forecast_Caminho =r"C:\Users\fsp_adolpho.salvador\Desktop\Konica Minolta\Desktop Cloud - Documentos\Desktop\FCST X RESULT\Forecast_Concat.xlsx"

forecast= pd.read_excel(forecast_Caminho,sheet_name='Sheet1')

forecast.columns

forecast=forecast.drop(columns=['saidas indireto', 'saidas SC','saidas POA', 'saidas PE'])


conn = sqlite3.connect('psi.db')

forecast.to_sql('forecast', conn, if_exists='replace', index=False)

conn.close()

