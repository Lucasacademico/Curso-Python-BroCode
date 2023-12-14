 # Fatiamento = Cria uma substring extraindo os elementos de outra string

nome = "Lucas Andrade"

# Fatiando o primeiro nome
primeiro_nome = nome[0:5] # [indexInicial:valorAcimaDoTamanho]
segundo_nome = nome[6:] # Não precisa especificar o valor final, pois irá direto pro final
nome_doido = nome[0:13:2] # O ultimo valor é step, que pula a quantidade especificada de char.
nome_reverso = nome[::-1]


print(primeiro_nome)
print(segundo_nome)
print(nome_doido)
print(nome_reverso)

