# Podemos detectar arquivos externos com o uso da biblioteca 'os'
# Pra esta aula, será criado um arquivo chamado arquivo.txt dentro da pasta desta aula. Recomendado já pegar o endereço de localização do arquivo.


# C:\Users\lrand\OneDrive\Área de Trabalho\Cursos\Python - BroCode\Lição 29 - Detectando arquivos

import os

# Criado variavel para inserir o endereço do arquivo
# Após colar o endereço, duplicar cada uma das contrabarras
path = "C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 29 - Detectando arquivos\\arquivo.txt"

# Verificando se o local do arquivo existe
if os.path.exists(path):
    print("Local do arquivo encontrado")
else:
    print("Local do arquivo não encontrado")

# Se excluirmos o arquivo, informará que o local do arquivo NÃO existe.
