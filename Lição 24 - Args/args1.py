# *args = Parâmetro que irá empacotar todos os argumentos em uma tupla.
# Útil para que uma função possa aceitar uma quantidade variável de argumentos.


# Criamos uma função com somente 2 parâmetros
def soma(num1, num2):
    soma = num1 + num2
    return soma


# Se tentarmos passar mais de 2 parâmetros ocorre um erro, pois há argumento a mais do que permitido pela função.
print(soma(1, 2, 3))
