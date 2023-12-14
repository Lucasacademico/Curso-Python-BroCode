# Aqui aprenderemos inserir informações em um arquivo externo

# 'r', 'w', 'a' - São os chars que específicam oq será feito no arquivo.
# 'r' - ler arquivos externos
# 'w' - Escrever/editar arquivos externos
# 'a' - Adicionar texto sobre o arquivo texto.


# Escrevendo no arquivo vázio externo teste.txt
# texto = "Eai\nIsso é um texto escrito em python\nTenha um bom dia"
texto = "Ops, texto alterado!"
with open("C:\\Users\\lrand\\OneDrive\\Área de Trabalho\\Cursos\\Python - BroCode\\Lição 31 - Escrevendo um arquivo\\teste.txt", 'w') as file:
    file.write(texto)
    # Obs: se alterarmos o conteúdo da var 'texto' e rodarmos o código, o texto no arquivo será alterado também.

'''
\n - Pula linha em arquivos externos, no geral já é incluso em todo inicio de print(), porém é uma funcionalidade invisível por assim dizer.
'''
