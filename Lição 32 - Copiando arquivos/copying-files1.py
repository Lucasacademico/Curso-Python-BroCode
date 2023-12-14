# copyfile(): copia o conteúdo de um arquivo.
# copy(): copyfile() + modo de permissão + diretório destino.
# copy2(): copy() + copias de metadados (criação de arquivo, e registro de modificações.)
# Para o uso destas funções precisaremos importar a biblioteca 'shutil'
# Criado o arquivo.txt com conteúdo que servirá de exemplo pra esta aula.

import shutil  # Biblioteca de copia de arquivos/conteúdos de arquivos

# Ativando o método copyfile(), selecionamos o arquivo que vamos copiar, e o nome do arquivo que será criado com a cópia do original.
shutil.copyfile('C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\Python - BroCode\\Lição 32 - Copiando arquivos\\arquivo.txt',
                'C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 32 - Copiando arquivos')  # src, dest
