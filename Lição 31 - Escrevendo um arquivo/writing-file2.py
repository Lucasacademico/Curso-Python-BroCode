# Como vimos no exemplo anterior, podemos inserir textos em um arquivo com o modo w(write), e se alterarmos o texto o valor será alterado também no arquivo externo.
# Agora veremos como inserir texto sem apagar ou alterar o arquivo com o modo 'a' de append.


# Primeiro adicionamos um texto inicial com 'w'
texto = "Linha 1 adicionada com o modo 'w'."
with open("C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 31 - Escrevendo um arquivo\\teste.txt", 'w') as file:
    file.write(texto)

# Depois podemos adicionar mais texto com o 'a'
texto2 = "\nLinha 2 adicionada com o modo 'a'."
with open("C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 31 - Escrevendo um arquivo\\teste.txt", 'a') as file:
    file.write(texto2)
