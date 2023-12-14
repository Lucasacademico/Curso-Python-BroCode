
# Inserindo Else no Try/except e Finally
try:
    numerador = int(input("Entre com um número para dividir: "))
    denominador = int(input("Entre com um número para ser dividido: "))
    result = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("Você não pode dividir por zero! Cabeça!!")
except ValueError as e:
    print(e)
    print("Insira somente números PFV")
except Exception as e:
    print(e)
    print("Algo deu errado!")
else:
    print(result) # Caso não ocorra nenhum erro, o resultado será imprimido.   
finally:
    print("Fim do programa") # O finally SEMPRE será executado