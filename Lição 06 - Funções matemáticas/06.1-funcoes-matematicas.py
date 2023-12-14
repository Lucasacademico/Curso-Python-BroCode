import math  # Importamos a biblioteca para podermos usar as funções Math

pi = 3.14

print(round(pi))  # Arredonda p/ o valor mais próximo.
print(math.ceil(pi))  # Arredonda p/ o valor mais alto.
print(math.floor(pi))  # Arredonda p/ o valor mais baixo

piNegativo = -3.14
# Valor absoluto mostra a distância desse valor para Zero - Sempre positivo.
print(abs(piNegativo))
print(pow(pi, 2))  # Potenciação - pi elevado a 2 nesse exemplo.
print(math.sqrt(pi))  # Verifica a raiz quadrada de um número

x, y, z = 1, 2, 3
print(max(x, y, z))  # Verifica o maior valor dentre as variaveis
print(min(x, y, z))
