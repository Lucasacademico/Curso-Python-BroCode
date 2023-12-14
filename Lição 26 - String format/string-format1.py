# str.format(): Método que dá aos usuários mais controle para a saída de dados.

animal = "cow"
item = "moon"

# Modo de impressão de strings com variáveis até o momento.
print("The " + animal + " jumped over the " + item)

# Utilizando o método format()
# A ordem das variaveis deve seguir a ordem das strings que queremos mostrar na frase.
print("The {} jumped over the {}".format(animal, item))

# Especificando ordem com o format()
print("The {1} jumped over the {0}".format(animal, item))
# Específicamos a ordem com a indexação. perceba que alterou a frase.

# Criando variavel dentro do format()
# Após criarmos as variaveis no format, basta colocarmos as variaveis nas chaves.
print("O {ser} roeu a roupa do {pessoa}".format(
    ser="rato", pessoa="rei de roma"))


# Outros módos de uso
texto = "The {} jumped over the {}"  # Criando a frase pronta
# Utilizando o format direto na VAR da frase.
print(texto.format(animal, item))
