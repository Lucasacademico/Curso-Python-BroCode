# Argumentos de palavras chaves: São argumentos precedidos por um identificados quando passamos eles para uma função.
# A ordem de argumentos não importa, diferente dos argumentos posicionais.
# Python entende os nomes dos argumentos que a função recebe.

def hello(primeiro, meio, ultimo):
    print("Olá " + primeiro + " " + meio + " " + ultimo)

# Perceba que a ordem dos argumentos muda o resultado da saída de dados
hello('Jubileu', 'Silva', 'Neto')
hello('Silva', 'Neto', 'Jubileu')