# Lista é usada para armazenar multiplos itens em uma única variavel.

# # Isto é uma simples lista de comida
# comidas = ["Pizza", "Hamburguer", "Hotdog", "Macarronada", "Bolo"]
# print(comidas) # Imprime as comidas na lista
# print(comidas[0]) # Imprime somente o elemento 0 da lista
# print(comidas[1])# Imprime somente o elemento 1 da lista
# # Obs: se tentarmos imprimir um elemento fora do index da lista, ocorre erro.

jogos = ["Super Mario", "Sonic", "Alex kidd", "Bomberman", "Zelda"]

# Adicionando um valor na lista
jogos[0] = "Doom"
print(jogos)  # Imprimido lista atualizada com Doom

# Iterando os valores da lista
for x in jogos:
    print(x)
