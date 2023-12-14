
nome = "Juju"

print("Olá, meu nome é {}. Prazer em te conhecer".format(nome))

# Podemos colocar também um espaço de caracteres para o uso das strings:
# dentro das chaves, inserimos :10, que é o máximo de string que irá mostrar na saída, entretanto, caso a string seja menor, o restante do espaço ficará a mostra, contando como espaço por cada "espaço não alocado".
print("Olá, meu nome é {:10}. Prazer em te conhecer".format(nome))

# Além do exemplo acima, podemos também definir o lado do espaço que a VAR vai ficar.
# O nome ficou à direita do espaço alocado.
print("Olá, meu nome é {:>10}. Prazer em te conhecer".format(nome))
# O nome ficou à esquerda do espaço alocado (padrão)
print("Olá, meu nome é {:<10}. Prazer em te conhecer".format(nome))
# O nome ficou no centro do espaço alocado.
print("Olá, meu nome é {:^10}. Prazer em te conhecer".format(nome))
