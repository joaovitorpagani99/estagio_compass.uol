#[Warm up] Em Python, declare e inicialize uma lista contendo o nome de 20 animais. 
# Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um (você pode utilizar list comprehension aqui).  
# Na sequência, armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.
import pandas as pd
animais = ["cachorro", "gato", "leão", "elefante", "tigre", "girafa", "zebra", "macaco", "panda", "lobo", "coala", "pinguim", "golfinho", "tartaruga", "cavalo", "peixe", "urso", "coruja", "crocodilo", "papagaio"]

animais.sort()

for animal in animais:
    print(animal)
    
nome_arquivo = "animais.csv"
df = pd.DataFrame(animais, columns=['Animais'])
df.to_csv(nome_arquivo, index=False)