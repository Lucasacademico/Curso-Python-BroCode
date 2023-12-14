# Podemos também criar uma variavel externa pra um nome, e inserir dentro da chamada da função para ser utilizada como parametro pro nome da função.

def hello(nome):
    print("Olá " + nome)
    print("Tenha um ótimo dia")


# Variavel nome
nome = 'Lucas'

# Chamada de função com var nome
hello(nome)

# Observação: parâmetros não são a mesma coisa que variaveis, por isso conseguimos criar uma variavel nome e utilizala no parametro nome da função. Mais informações sobre variaveis locais e globais serão passadas em outras lições.
