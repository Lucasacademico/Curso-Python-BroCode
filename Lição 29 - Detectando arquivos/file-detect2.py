# Verificando se o arquivo existe caso o arquivo esteja específico no endereço.
# Verificando também se não é um diretório
# IMPORTANTE: O que vai dizer se o que está sendo verificado é um arquivo ou pasta, é a ultima parte do endereço, que, caso seja o nome do arquivo (e existir no endereço correrto), será considerado um arquivo, ou caso a ultima parte do endereço seja na pasta existente, será considerada uma pasta (SE estivermos analisando com os devidos comando - isfile/isdir)

import os

path = "C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 29 - Detectando arquivos\\arquivo.txt"

# Verificando se é um arquivo ou pasta
if os.path.exists(path):
    print("Local do arquivo encontrado")
    if os.path.isfile(path):
        print("Isto é um arquivo")
    elif os.path.isdir(path):
        print("Isto e uma pasta")
else:
    print("Local do arquivo não encontrado")
