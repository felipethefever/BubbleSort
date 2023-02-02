lista = [1, 27, 48, 65, 83, 14, 8, 41, 58, 6, 94, 77, 9, 12, 28, 2, 33, 55]


def bubble_sort(arr):
    n = len(arr)

    # Para cada elemento i do array
    for i in range(n):

        # Para cada elemento j do array
        for j in range(0, n - i - 1):

            # Se elemento i for maior que elemento j
            if arr[j] > arr[j + 1]:
                # Troque os elementos i e j
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort(lista))
