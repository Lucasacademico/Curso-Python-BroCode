# Formatando números com o format()

pi = 3.14159
# limiando espaço de duas casas decimais.
print("O número pi é {:.2f}".format(pi))

x = 1000
print("O número é {:,}".format(x))  # Podemos inserir a virgula nos números
print("O número é {:b}".format(x))  # Formatando para binário
print("O número é {:o}".format(x))  # Formatando para números octais
print("O número é {:X}".format(x))  # Formatando para números hexadecimais
print("O número é {:E}".format(x))  # Formatando para notação ciêntifica
