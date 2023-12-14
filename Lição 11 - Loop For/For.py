"""
Loop FOR:
- Executa um bloco de código uma quantidade limitada de vezes.
- Loop While pode executar ilimitadamente.
- For Loop executa limitadamente.
"""

import time #Não explicado, mas necessário pro exemplo que usamos a função 'time'

# # printa um valor i com range de tamanho 10 (no caso, de 0 à 9)
# for i in range(10):
#     print(i+1) # i+1 para imprimir de 1 à 10

# # Printa os valores de 50 até 99 
# for i in range(50, 100):
#     print(i)

# # Printa cada caracter do nome
# for i in "Lucas Andrade":
#     print(i)

# Contagem regressiva de 10 à 1, contando -1
for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1) # Imprime apenas um valor por segundo, como uma contagem de segundos.
print("Feliz ano novo!!!")
 