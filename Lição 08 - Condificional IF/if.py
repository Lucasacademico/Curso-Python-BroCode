# Condicional IF é um bloco de codigo que irá executar se a condição for verdadeira.

idade = int(input("Qual sua idade? "))

# Blocos IF
if idade < 0:
    print("Você ainda não nasceu!")
elif idade >= 18:
    print('Você é um adulto!')
elif idade == 100:
    print("Você é um centenário!")
else: 
    print('Você é de menor!')
# Obs: A ordem de ifs é importante, da maior pra menor.