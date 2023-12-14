# Tuplas: Coleção que é ordenada e inalterável, usada para agrupar dados relacionados.

estudante = ("Lucas", 27, "Homem")

# Imprimindo tupla
print(estudante)

# Verificando quantos "Lucas" tem na tupla
print(estudante.count("Lucas"))

# Verificando o index do valor "Homem"
print(estudante.index("Homem"))

# Imprimindo os valores da tupla separadamente
for x in estudante:
    print(x)

# Verificando se um valor está na tupla
if "Lucas" in estudante:
    print("Lucas esta na tupla")