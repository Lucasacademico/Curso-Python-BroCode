# Declarando um retorno: Funções enviam ao python valores/objetos de volta para quem chama. Estes valores/objetos são conhecidos como o valor retornado.

# Função para multiplicação de valores
def multiplicacao(num1, num2):
    result = num1 * num2  # variavel interna da função recebendo a multiplicação dos parametros
    return result  # Retorno do resultado que será retornado da funçaõ


# Chamada da função não printa o resultado em tela, pois na função não existe um print deste resultado. Funções com retorno sem print, precisam de um método que imprima o valor calculado.
multiplicacao(5, 9)

# Printando a função
print(multiplicacao(5, 9))
