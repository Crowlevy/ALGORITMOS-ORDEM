import random 
from time import time
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Verifica se o filho esquerdo existe e é maior que o pai.
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # Verifica se o filho direito existe e é maior que o pai ou o maior filho esquerdo.
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca o pai com o maior filho.
        heapify(arr, n, largest)  # Chama recursivamente para o filho modificado.

def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo a partir do array.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos do heap um por um.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move o elemento raiz (maior) para o final.
        heapify(arr, i, 0)  # Chama heapify no heap reduzido.

# Exemplo de uso
arr = [random.randint(1,1000000000) for _ in range(2000000)]
tempo_inicial=time()
heap_sort(arr)
tempo_final=time()
print("Array ordenado:", arr)
print(f"Tempo Total:{tempo_final-tempo_inicial}")