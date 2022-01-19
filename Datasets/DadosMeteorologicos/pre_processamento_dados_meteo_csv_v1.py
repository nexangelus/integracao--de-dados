# Importacao de bibliotecas
import os
import numpy as np
import pandas as pd
from google.colab import data_table
data_table.enable_dataframe_formatter()

# Cria lista de ficheiros CSV
csv_files = []
for file in os.listdir(os.getcwd()):
  if file.endswith('.csv'):
    csv_files.append(file)

# Retira linhas com nomes das Estacoes dos ficheiros CSV; enconding 'windows-1252'
df_header_nomes = pd.read_csv(csv_files[1], encoding='windows-1252', header = 1)
df_header_nomes.drop(df_header_nomes.columns[-1], axis=1, inplace=True)

# Cria lista com nomes das estacoes meteo
col_names = []
for i in range(1, len(df_header_nomes.columns), 8):
     col_names.append(df_header_nomes.columns[i])

# Corta código do nome das Estacoes Meteorológicas 
for i in range(0, len(col_names), 1):
  index_cut = col_names[i].rfind("(")
  col_names[i] = col_names[i][0:index_cut-1]

# Cria dataframe com dados das estacoes meteo
df = pd.read_csv(csv_files[1], encoding='windows-1252', header = 2)
df.drop(df.columns[-1], axis=1, inplace=True)
df.rename(columns={'Unnamed: 0':'Data'}, inplace=True)

# Guarda dados de cada estacão num ficheiro CSV
j=0
for i in range(1,len(df.columns),8):
  df_new = pd.concat([df.iloc[:,0], df.iloc[:,list(range(i,i+8))]], axis= 1)
  df_new.rename(columns={0:'Data'}, inplace=True)
  df_new.insert(0, 'Nome_Estacao', "")
  df_new['Nome_Estacao'] = col_names[j]
  df_new.to_csv(col_names[j] + '.csv', index = False)
  j = j+1
  