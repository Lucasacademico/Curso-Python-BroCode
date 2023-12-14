# Nested loops = O "looping interno" irá terminar todas as suas interações. antes de terminar uma iteração do "looping externo".
# Resumindo, é um looping dentro de outro.

linhas = int(input("Quantas linhas: "))
colunas = int(input("Quantas colunas: "))
simbolo = input("Insira um símbolo pra usar: ")

for i in range(linhas):
    for j in range(colunas):
        print(simbolo, end="")
    print()