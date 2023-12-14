
# Criando exceptions para arquivo inexistente OU endereço incorreto.
try:
    with open("C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 30 - Lendo arquivos\\arquivo.txsst") as file:
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("Verifique se o arquivo existe ou o endereço está correto.")
