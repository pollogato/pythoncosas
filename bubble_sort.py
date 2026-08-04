
lista = [1, 2, 3, 1, 4, 4, 1, 6, 0, 5, 3, 9, 4]


# Recorre la lista tantas veces como elementos tiene
for i in range(len(lista)):
    pos = 0

    # Compara cada elemento con el siguiente
    while pos < (len(lista) - 1):

        # Si el elemento actual es mayor que (>) el siguiente,
        # se intercambian de posición
        if lista[pos] > lista[pos + 1]:
            aux = lista[pos + 1]
            lista[pos + 1] = lista[pos]
            lista[pos] = aux

        # Avanza a la siguiente posición
        pos = pos + 1

# Muestra la lista ordenada de menor a mayor
print(lista)