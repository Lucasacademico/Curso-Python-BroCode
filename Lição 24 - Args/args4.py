# Empacotando o args pra lista, e depois para tuplas

def soma(*args):
    soma = 0
    args = list(args)  # transformando o args em lista
    args[0] = 0  # Informando que o index 0 será sempre 0
    for i in args:
        soma += i
    return soma


# Perceba que independente do valor inserido no index 0, o valor dele contará como 0 na soma.
print(soma(1, 2, 3, 4, 5))
