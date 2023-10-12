from time import time
import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o ponto médio da lista.
        left_half = arr[:mid]  # Divide a lista em duas metades.
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursivamente ordena a metade esquerda.
        merge_sort(right_half)  # Recursivamente ordena a metade direita.

        i = j = k = 0

        # Junta as duas metades ordenadas de volta em uma única lista.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se algum elemento foi deixado nas metades esquerda ou direita.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Exemplo de uso
arr = [random.randint(1,1000000000) for _ in range(2000000)]
tempo_inicial=time()
merge_sort(arr)
tempo_final=time()
print("Array ordenado:", arr)
print(f"TEMPO TOTAL:{tempo_final-tempo_inicial}")