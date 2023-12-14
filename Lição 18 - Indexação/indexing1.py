# Operador index: Dá acesso a uma sequência de elementos (str, list, tuples)

nome = 'lucas Andrade!'

# Verificando o primeiro caracter do nome, e caso minusculo, utilizar método capitalize().
if (nome[0].islower()):
    nome = nome.capitalize()
print(nome) # Imprime o nome atualizado com o capitalize.

# Pegando apenas o primeiro nome e passando para uma var com a indexação e em maisculo.
primeiro_nome = nome[0:5].upper() # poderia ser só [:5] 
print(primeiro_nome)

# Pegando o sobrenome, transformando em maisculo, e passando para uma var.
sobrenome = nome[6:].upper() 
print(sobrenome)

# Pegando o ultimo caractere de exclamação
exclamacao = nome[-1]
print(exclamacao)