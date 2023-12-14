# Vamos aprimorar os blocos de excessões com mais casos de possíveis erros, sempre testando se irão adentrar o bloco quando as falhas forem disparadas.

try:
    numerador = int(input("Entre com um número para dividir: "))
    denominador = int(input("Entre com um número para ser dividido: "))
    result = numerador / denominador
    print(result)
except ZeroDivisionError:
    print("Você não pode dividir por zero! Cabeça!!")
# Except de string no lugar de número
except ValueError:
    print("Insira somente números PFV")
# except Exception:
#     print("Algo deu errado!")
