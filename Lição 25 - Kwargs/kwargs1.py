# **Kwargs: Parametros que podem empacotar todos os argumentos em um dicionário.
# Útil para que uma função possa aceitar uma quantidade variável de argumentos de palavras-chave.

# Exemplo simples - Utilizando o **kwargs como argumentação, podemos inserir os valores que queremos a saída, sem precisar colocar um argumento pra cada saída de dado. Porém, a qtd de saída é Limitada.
def hello(**kwargs):
    print("Hello " + kwargs['primeiro'] + " " + kwargs['ultimo'])

# Mesmo que só serão utilizados somente dois argumentos sobre o **kwargs, podemos inseri multiplos, visto que o uso do **kwargs possibilita multiplas argumentações, mesmo que as saídas não estejam específicadas na função.
hello(primeiro = 'Jubileu', segundo = 'Silva', ultimo = 'Neto')