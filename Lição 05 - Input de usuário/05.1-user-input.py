# Input - Recebe um valor do usuário, e pode ser armazenado em uma variavel

# Input com variavel
nome = input("Qual seu nome? ")
# Type cast para receber o valor da idade em inteiro
# Se tentarmos colocar um valor float, ocorrerá erro, visto que o type casting é pra valores INTEIROS.
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? "))

print("Hello " + nome)
# Type cast pra str pra podermos imprimir os valores concatenados
print("Você tem " + str(idade) + " anos de idade")
print("Sua altura é " + str(altura) + " cm.")
