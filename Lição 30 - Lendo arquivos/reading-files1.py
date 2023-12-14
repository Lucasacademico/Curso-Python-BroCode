# Leitura de arquivos.
# Arquivo criado na pasta desta lição para testes.


# Abrindo o arquivo
with open("C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 30 - Lendo arquivos\\arquivo.txddt") as file:
    print(file.read())

    # Obs: usando o módo 'with open()', fecha o arquivo automáticamente, se fosse só 'open()', deveriamos fechar manualmente.

# Verifica se o arquivo foi fechado - Bool.
print(file.closed)
