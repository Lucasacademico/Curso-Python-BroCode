
# Slice do site google
# Só vamos imprimir o google
website = "http://google.com"
# o primeiro parametro contamos a qtd de chars antes do google, o segundo parametro contamos a quantidade de chars depois do google e colocamos negativo.
slice = slice(7, -4)
print(website[slice])
