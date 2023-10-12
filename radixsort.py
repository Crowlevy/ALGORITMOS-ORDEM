import random
from time import time
def RadixSort(n):
    maxNums = max(n)
    exp = 1
    while maxNums//exp>0:
        contagem(n,exp)
        exp*=10
def contagem(n,exp):
    num = len(n)
    saida = [0]*num
    count = [0]*10

    for i in range(num):
        index = (n[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i = num-1
    while i>=0:
        index=(n[i]//exp)%10
        saida[count[index] - 1]=n[i]
        count[index]-=1
        i-=1
    for i in range(num):
        n[i]= saida[i]

listaNumeros=[random.randint(1,1000000000) for _ in range(2000000)]
tempo_inicial= time()
RadixSort(listaNumeros)
tempo_final = time()
print(listaNumeros)
print(f"TEMPO TOTAL:{tempo_final-tempo_inicial}")