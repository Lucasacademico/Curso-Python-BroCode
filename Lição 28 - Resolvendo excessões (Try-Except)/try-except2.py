# Utilizando o algoritmo anterior com try/except

# Criando a excessão do erro para não causar o erro.
try:
    numerador = int(input("Entre com um número para dividir: "))
    denominador = int(input("Entre com um número para ser dividido: "))
    result = numerador / denominador
    print(result)
except Exception:
    print("Algo deu errado!")

# Obs: não é considerado boa prática ter apenas um bloco de excessões para os erros, o certo é ter multiplos blocos para cada tipo de excessões que possam acontecer.
