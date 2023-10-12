import random
'''Stalin Sort é um algoritmo completamente feito no meme, ele pega uma determinada array de números e os que estiverem fora de 
   ordem ele simplesmente apaga e deixa somente os que estão em ordem naturalmente, ele foi feito com o intuito de ser
   uma brincadeira e não deve ser usado em listas que precisam de ordenação'''
def stalinSort(n):
    resultado = [n[0]]
    for i in range(1,len(n)):
        if n[i] >= resultado[-1]:
            resultado.append(n[i])
    return resultado
listaNumeros = [random.randint(1,1000000000) for _ in range(2000000)]
ordem=stalinSort(listaNumeros)
print(ordem)