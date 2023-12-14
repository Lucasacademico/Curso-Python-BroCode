# listas dentro de listas

drinks = ["Café", "Soda", "Chá"]
jantar = ["Pizza", "Hamburguer", "Hotdog"]
doces = ["Bolo", "Sorvete"]

comidas = [drinks, jantar, doces]

print(comidas)  # Imprimindo as listas dentro lista comidas
print()

print(comidas[0])  # Imprimindo a lista drinks dentro da lista comidas
print(comidas[1])  # Imprimindo a lista jantar dentro da lista comidas
print(comidas[2])  # Imprimindo a lista doces dentro da lista comidas

print()

# Imprindo um valor específico
# Imprimindo Hamburguer
print(comidas[1][1])  # Endereço do hamburguer na indexação das listas.]

# Imprimindo Chá
print(comidas[0][2])
