# Utilizando o *args

# Utilizamos o *args como argumento, declaramos a soma = 0, e criamos um laço for dentro de args, que soma cada argumento entre si.
def soma(*args):
    soma = 0
    for i in args:
        soma += i 
    return soma

# Chamada da função com múltiplos argumentos, podendo ser inserido números à critério dos usuários.
print(soma(1, 2, 3, 4, 5))