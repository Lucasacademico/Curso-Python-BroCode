nome = "LucasAndrade"

# Metodos String
print(len(nome))  # conta a qtd de caracteres - Espaço conta tbm.
print(nome.find("d"))  # Verifica o index da(s) letra(s) que estamos buscando.
# Deixa toda a string capitaliza - Só a primeira letra maiscula
print(nome.capitalize())
print(nome.lower())  # Deixa toda a string minuscula
print(nome.upper())  # Deixa toda a string maiscula
print(nome.isdigit())  # Verifica se a string é um digito - retorna bool
# Verifica se a string são valores alfabéticos - Se houver espaço na string retorna false
print(nome.isalpha())
# Conta a quantidade de um char es específico - Conta espaço tbm se colocarmos como o parametro.
print(nome.count("a"))
# Troca um char por outro - precisa de dois parametros.
print(nome.replace("u", "o"))
print(nome*3)  # mostra o numero x vezes
