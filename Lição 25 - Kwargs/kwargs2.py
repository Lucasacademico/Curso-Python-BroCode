
# Utilizando Kwargs com saídas ilimitadas
def hello(**kwargs):
    result = 0
    print("Olá", end=" ")
    # Transforma o kwargs em ítens para acessarmos diretamento os valores do dicionário
    for chave, valor in kwargs.items():
        print(valor, end=" ")


# Os argumentos na chamada da função são chaves:valores
hello(primeiro='Jubileu', ultimo='Neto', segundo='Silva')
