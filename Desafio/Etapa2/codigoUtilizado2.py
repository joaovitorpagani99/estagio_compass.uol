import requests
import pandas as pd
import json
import boto3
from io import StringIO
from datetime import datetime


##Decidir pegar do omdb tambem, pois o imdb nao tem muitos dados, e vi que o omdb teria alguns dados complementares
## e como ele limita a 1000 requisições por dia, decidi pegar apenas os filmes de 2020 a 2015.
chave_api = 'c7507d72'

s3 = boto3.client('s3')
s3_arquivo = 'Raw/Local/CSV/Movies/2023/7/22/movies.csv'
response = s3.get_object(Bucket='data-lake-paganipb', Key=s3_arquivo)

csv = response['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(csv), sep="|", low_memory=False)

df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce')
df_filtrados = df[(df['anoLancamento'] == 2020) & (df['genero'].str.contains('Horror|Mystery', case=False))]

df_agrupados = df_filtrados.groupby('id')

filmes = []

contador_requisicoes = 0

for id_filme, group_df in df_agrupados:
    if contador_requisicoes >= 1000:
        break
    
    id_filme = id_filme.strip() 
    url = f"http://www.omdbapi.com/?i={id_filme}&apikey={chave_api}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta da API é bem-sucedida
        
        data = response.json()

        df = {
            'id': data.get('imdbID'),
            'titulo': data.get('Title'),
            'data de lancamento': data.get('Released'),
            'bilheteria': data.get('BoxOffice'),
            'Awards': data.get('Awards'),  
            'Avaliacao do imdb': data.get('imdbRating'),
            'imdbVotes': data.get('imdbVotes'),
            'Metascore': data.get('Metascore')
        }

        filmes.append(df)
        contador_requisicoes += 1
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para {url}: {e}")

df_result = pd.DataFrame(filmes)

json_data = df_result.to_json(orient='records', lines=True)

data = datetime.now().strftime('%Y/%m/%d')
nomeJson = 'prt-uty-nfd.json'
json_key = f"Raw/Omdb/JSON/{data}/{nomeJson}"
s3.put_object(Bucket='data-lake-paganipb', Key=json_key, Body=json_data)
