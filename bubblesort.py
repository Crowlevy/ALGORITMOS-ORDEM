import random 
'''Aqui temos um exemplo básico do mais simples algoritmo de ordenação chamado BubbleSort, ele é usado para projetos
   relativamente pequenos e que não precisem de tanta performace. Ele é inviável quando é trabalhado com lista enorme'''
def bublesort(n):
    aux = len(n) #Aqui criei uma auxiliar que vai servir para armazenar somente o tamanho da lista
    for i in range(aux):
        for j in range(0,aux-i-1):#Quando criado o for j, ele vai percorrendo por toda a lista e testando cada vez os números,caso seja maiores ou menores ele joga pra frente ou para trás
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]#Se a lista do índice j for maior que ela do indíce j+1, significa que esse número deve ser já jogado para um dos ultimos
listaNumeros= [random.randint(1,1000000000) for _ in range(2000000)]
bublesort(listaNumeros)
print(listaNumeros)