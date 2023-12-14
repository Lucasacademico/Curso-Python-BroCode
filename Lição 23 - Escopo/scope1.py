# Escopo: É a região cuja a variável é reconhecida.
# Uma variável é somente liberada dentro da região que foi criada.
# As versões de um escopo podem ser criadas localmente ou globalmente.

'''
    Tipos de escopos:
    - L(Local): Locais
    - E(Enclosing): Variaveis de enclaususarmento
    - G(Global): Variaveis globais
    - B(Built-in): Variaveis Built-in
'''

# Exemplo simples de uma variavel global
nome = 'Lucas'

# Exemplo de uma variavel local


def display_name():
    nome = 'Andrade'  # Variavel reconhecida somente dentro desta função.
    print(nome)


# Chamada da variavel global
# Perceba que a variavel printada foi a variavel global 'nome' com valor 'Lucas'
print(nome)

# Chamada da variavel local
# Perceba que a variavel printada é referente à var local 'nome' com valor 'Andrade'. Provando que ambas não se enxergam.
display_name()
