# Passando um parâmetro numerico

def hello(nome, sobrenome, idade):
    print("Olá " + nome + " " + sobrenome)
    print("Você tem " + str(idade) + " anos de idade")
    print("Tenha um ótimo dia")
    # é importante não esquecer de realizar o type casting no parametro numérico para str.

sobrenome = 'Andrade'

# Chamada de função com nome str, sobrenome de variavel, e valor inteiro.
print('Lucas', sobrenome, 25)