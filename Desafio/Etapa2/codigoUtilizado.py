import pandas as pd
import requests
import boto3
from io import StringIO
from datetime import datetime
import json
import sys

chave_api = 'f8c69e755ba2b6a393e2ef3b79b7715a'
s3_bucket = 'data-lake-paganipb'
s3_arquivo = 'Raw/Local/CSV/Movies/2023/7/22/movies.csv'
s3 = boto3.client('s3')

data_atual = datetime.now().strftime('%Y/%m/%d')
arquivo = s3.get_object(Bucket=s3_bucket, Key=s3_arquivo)

csv = arquivo['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv), sep="|", low_memory=False)

def obter_detalhes_filme(id_filme, chave_api):
    url = f'https://api.themoviedb.org/3/movie/{id_filme}?&api_key={chave_api}'
    arquivo = requests.get(url)
    if arquivo.status_code == 200:
        df = arquivo.json()
        return df
    else:
        return None

df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce')
df_filtrados = df[(df['anoLancamento'] >= 2015) & (df['anoLancamento'] <= 2020) & (df['genero'].str.contains('Horror|Mystery', case=False))]
df_agrupados = df_filtrados.groupby('id')
filmes = []

for id_imdb, grupo in df_agrupados:
    id_filme = grupo['id'].values[0]
    detalhes_filme = obter_detalhes_filme(id_filme, chave_api)
    if detalhes_filme:
        filmes.append(detalhes_filme)


limite_tamanho_json = 10 * 1024 * 1024
partes_json = []
parte_atual = []
tamanho_atual = 0

for detalhes_filme in filmes:
    df_result = pd.DataFrame(detalhes_filme)
    filme_json = json.dumps(df_result)
    tamanho_json_filme = sys.getsizeof(filme_json)
    if tamanho_atual + tamanho_json_filme <= limite_tamanho_json:
        parte_atual.append(detalhes_filme)
        tamanho_atual += tamanho_json_filme
    else:
        partes_json.append(parte_atual)
        parte_atual = [detalhes_filme]
        tamanho_atual = tamanho_json_filme

if parte_atual:
    partes_json.append(parte_atual)

for idx, parte in enumerate(partes_json):
    json_str = json.dumps(parte)
    s3_saida = f'Raw/Tmdb/JSON/{data_atual}/prt-uty-nfd_part{idx + 1}.json'
    s3.put_object(Body=json_str, Bucket=s3_bucket, Key=s3_saida)
