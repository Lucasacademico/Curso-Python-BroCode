# Para uso de números gerados randomicamente, devemos utilizar a biblioteca random

import random

# Gerando um número randomico inteiro entre 1 e 6
# Cada ves que rodarmos o código o número muda.
x = random.randint(1, 6)  # método de random de valores inteiros entre 1 e 6
print(x)

# Gerando um número decimal entre 0 e 1
y = random.random()  # Método de random número de 0 à 1
print(y)

# escolhendo um valor da lista
jankenpo = ['pedra', 'papel', 'tesoura']
z = random.choice(jankenpo)  # método de escolha
print(z)

# Misturando cartas de baralho
cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "k", "A"]
random.shuffle(cartas)  # Médodo de misturar os valores
print(cartas)
