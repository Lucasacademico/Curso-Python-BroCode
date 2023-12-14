capitais = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

# Inserindo novo valor no dicionário
capitais.update({'Germany': 'Berlim'})

# Alterando um valor existente do dicionário
capitais.update({'USA': 'Las Vegas'})

# Removendo chave:valor China
capitais.pop('China')

# Imprimindo chaves:valores inseridos/alterados/removidos.
for keys, values in capitais.items():
    print(keys, values)

# Remove todos as chaves:valores do dicionario
capitais.clear()

if capitais == {}:
    print('Todos as chaves:valores foram removidas com o método clear')
else:
    print('Algo deu errado')
