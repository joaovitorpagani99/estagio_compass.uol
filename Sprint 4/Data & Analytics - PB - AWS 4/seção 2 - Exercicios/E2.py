def conta_vogais(texto:str)-> int:
    
    vogais = ['a', 'e', 'i', 'o', 'u']

    # Filtra apenas os caracteres que são vogais
    vogais_presentes = list(filter(lambda x: x.lower() in vogais, texto))

    # Retorna a contagem das vogais presentes
    return len(vogais_presentes)