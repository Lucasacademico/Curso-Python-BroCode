# Exception: eventos detectados durante uma execução que geralmente interrompem o fluxo de um programa.
# O uso do except é justamente evitar que tais eventos não interrompam o funcionamento do código.

# Exemplo simples - Neste pequeno algoritmo de divisão, tente dividir por 0, e perceba que ocorre o erro ZeroDivisionError
numerador = int(input("Entre com um número para dividir: "))
denominador = int(input("Entre com um número para ser dividido: "))
result = numerador / denominador
print(result)
