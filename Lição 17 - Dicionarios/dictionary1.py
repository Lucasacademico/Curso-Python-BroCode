# Dicionários: Uma colação alterável, não-ordenada de chaves:valores páres únicos.
# Rápido devido ao uso de Hash, permitindo acesso rápido dos valores

capitais = {
    'USA': 'Washington DC',
    'India': 'New Dehli', 
    'China': 'Beijing',
    'Russia': 'Moscow'
}

# Modos de impressão
print(capitais)
print(capitais['USA']) # chamada de valor pela chave
print(capitais.get('China')) # chamada de valor por get. Obs: se tentarmos pegar uma chave não-existente, o retorno será 'None', em vez de ocorrer um erro. É uma maneira mais segura.
print(capitais.keys()) # Imprime somente as chaves (sem os valores)
print(capitais.values()) # Imprime somente os valores sem chaves.
print(capitais.items()) # Imprime as chaves: valores como itens.



