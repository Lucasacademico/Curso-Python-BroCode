# Gerando uma VAR especificando o erro/falha no except

# Gerando a variavel no erro e imprimindo essa variavel
try:
    numerador = int(input("Entre com um número para dividir: "))
    denominador = int(input("Entre com um número para ser dividido: "))
    result = numerador / denominador
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("Você não pode dividir por zero! Cabeça!!")
except ValueError as e:
    print(e)
    print("Insira somente números PFV")
except Exception as e:
    print(e)
    print("Algo deu errado!")


# Imprimir a variavel do erro vai imprimir o nome do erro.
