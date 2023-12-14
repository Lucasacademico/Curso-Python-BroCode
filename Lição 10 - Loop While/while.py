# O while loop irá executar um bloco de código, desde que a condição seja verdadeira.

# # Exemplo simples 1:
# while 1 == 1:
#     nome = print("Socorro, tô preso em um loop.")

# Exemplo 2 - Só sairá do loop, se digitar o nome (no caso, se a qtd de chars for maior que 0).
nome = None # Podemos inserir o None pra dizer que não tem nada na variavel.
while len(nome) == 0:
    nome = input("Digite seu nome: ")
print("Olá "+nome)

