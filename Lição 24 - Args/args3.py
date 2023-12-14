# Podemos alterar o nome do *args para qualquer coisa e o funcionamento será o mesmo.

def soma(*oi):
    soma = 0
    for i in oi:
        soma += i
    return soma


print(soma(1, 2, 3, 4, 5))
