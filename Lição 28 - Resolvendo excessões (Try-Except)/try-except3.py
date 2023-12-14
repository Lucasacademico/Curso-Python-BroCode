# Criando excessões específicas para erros específicos.

# Reaproveitando o código anterior, vamos inserir mais um bloco de excessão, dessa vêz específico para o erro de denominador = 0.
try:
    numerador = int(input("Entre com um número para dividir: "))
    denominador = int(input("Entre com um número para ser dividido: "))
    result = numerador / denominador
    print(result)
except ZeroDivisionError:
    print("Você não pode dividir por zero! Cabeça!!")
except Exception:
    print("Algo deu errado!")

# Desta vez o erro de divisão por zero foi ativado logo após a falha, visto que criamos a excessão para este caso específico.
