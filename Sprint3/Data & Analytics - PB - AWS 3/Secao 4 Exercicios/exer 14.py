def minha_funcao(*args, **kwargs):
    for a in args:
        print(a)
    for k in kwargs.items():
        print(k[1])

minha_funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa',x=20)