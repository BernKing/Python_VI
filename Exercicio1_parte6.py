# bubble sorter com verificação


lista = [123, 2424, 43434, 213, 12, 2, 4, 12412414]
n = len(lista)

troca = False

for i in range(n - 1):
    for j in range(0, n - 1 - i):

        if lista[j] > lista[j + 1]:
            troca = True
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

    if not troca:
        break

print(lista)
