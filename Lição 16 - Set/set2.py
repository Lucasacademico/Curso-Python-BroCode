
utensilios = {"Garfo", "Colher", "Faca"}
prataria = {"Prato", "Copo", "Panelas"}

utensilios.clear() # Excluindo todos os valores da prataria

# Atualizando todos os valores do UTENSILIO com os valores da PRATARIA
utensilios.update(prataria) 

# Imprimindo o set utensílios com os valores atualizados da prataria
for x in utensilios:
    print(x)
print()