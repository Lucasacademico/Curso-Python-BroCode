# Loop control statement: Altera uma execução de looping de sua sequência normal.

# break: usado para finalizar o loop totalmente
# continue: pula para a proxima iteração do looping
# pass: não faz nada, serve como um placeholder (espaço reservado)

# # Exemplo: Dentro do while, o usuário digita o nome, e caso o nome for maior (nada digitado), quebra o loop.
# while True:
#     nome = input("Digite seu nome: ")
#     if nome != "":
#         break

# # Exemplo 2: Existe um numero com traços, o loop for vai iterar cada valor dessa string, e SE um valor for um '-'(traço), irá continuar (PULAR) para a proxima iteração sem imprimir o traço.
# num_tel = "123-456-7890"
# for i in num_tel:
#     if i == "-":
#         continue
#     print(i, end="")
#     # o end="" serve pra colocar cada iteração do for na mesma linha, e não em linhas separadas.

# Exemplo 3: O código simplesmente irá PASSAR o número 13, e imprimir os outros, porém o valor ainda esta lá, só não será imprimido.
for i in range(1, 21):
    if i == 13:
        pass
    else: 
        print(i, end=" ")
