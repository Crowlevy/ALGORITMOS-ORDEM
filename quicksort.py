import random
from time import time
"""O QuickSort é considerado por muitos o melhor algoritmo de ordenação, sendo extremamente rápido com listas grandes 
   ele é o mais performático dentre todos os outros, mas como qualquer algoritmo também existem limitações como se no caso
   tiver uma sequência muito grande pode haver crashses"""
def quicksort(n):
    if len(n)<=1:#Pegando o tamanho da lista e  caso sobre um algarismo ou menos que isso, ele só irá retornar a lista por completo
        return n
    pivo = random.choice(n)#Declarando o 'PIVÔ' aleatoriamente, esse que vai auxiliar por todo o processo de ordenação
    menor= [x for x in n if x<pivo]
    igual = [x for x in n if x==pivo]
    maior = [x for x in n if x>pivo]
    '''Nessa parte declaramos 3 variáveis que serão testadas a partir do pivo e mandando para onde devem ficar'''
    return quicksort(menor)+ igual + quicksort(maior)#Estamos retornando o a função pegando o menor numero e concatenando com o igual e maior número da função, sendo assim possível uma ordem simples e eficaz

listaNumeros= [random.randint(1,1000000000) for _ in range(2000000)]

tempo_inicial= time()
ordem=quicksort(listaNumeros)
tempo_final= time()

print(ordem)
print(f"Tempo total:{tempo_final-tempo_inicial}")