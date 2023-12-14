# Passando a função para uma variavel

def multiplicacao(num1, num2):
    result = num1 * num2  
    return result  

# Uma maneira inteligente é passar a função para uma variavel com os parametros que queremos calcular
x = multiplicacao(5,7)

# Chamada da variavel criada da função para imprimir o valor
print(x)