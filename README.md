# PSI Data Management

Este projeto é um conjunto de scripts em Python para manipulação, tratamento e consultas de dados relacionados às operações da Konica Minolta. Ele utiliza o SQLite para armazenamento de dados e Pandas para processamento.

## Estrutura do Projeto

- **alteracao_sql.py**: Script para alterar a estrutura de tabelas no banco de dados SQLite.
- **consultas.py**: Realiza consultas específicas no banco de dados e exporta os resultados para análise.
- **juntanto_tabelas.py**: Une tabelas no banco de dados usando cláusulas JOIN.
- **sql_teste.py**: Cria a estrutura inicial do banco de dados com tabelas e colunas necessárias.
- **tratar_imputar_FCST.py**: Carrega e trata dados de previsão (forecast) de um arquivo Excel para o banco de dados.
- **tratar_imputar_zmb51.py**: Trata e importa dados de consumo (ZMB51) para o banco de dados.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: `pandas`, `sqlite3`, `openpyxl`

## Como Usar

1. Instale os pacotes necessários:
   ```bash
   pip install pandas openpyxl
