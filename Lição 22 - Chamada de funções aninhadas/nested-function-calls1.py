# Chamada de funções aninhadas: Chamada de funções dentro de outras funções chamadas.
# Funções internas são resolvidas primeiro
# Valor retornado é usado como um argumento para a função externa.


# Exemplo de alterações de um valor com diversos métodos em várias linhas
# Recebe um valor numérico em formato string
num = input("Digite um float negativo ")
num = float(num)  # Transformando o valor string negativo em float
num = abs(num)  # Transforma o valor float em um valor absoluto (positivo)
num = round(num)  # arredonda o valor para o num mais próximo
print(num)  # Imprime o valor final
