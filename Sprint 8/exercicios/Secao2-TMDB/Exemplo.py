import requests
import pandas as pd

from IPython.display import display

##Retirei a chave conforme o solicitado no exemplo, mas na pasta de evidencias está la que roudou. 

api_key = ""

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"
url = f"https://api.themoviedb.org/3/certification/movie/list"


response = requests.get(url)
data = response.json()



filmes = []



for movie in data['results']:
    df = {'Titulo': movie['title'],
    'Data de lançamento': movie['release_date'],
    'Visão geral': movie['overview'],
    'Votos': movie['vote_count'],
    'Média de votos:': movie['vote_average']}



filmes.append(df)


df = pd.DataFrame(filmes)
display(df)