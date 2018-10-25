nome = str(input('Digite seu nome completo: '))
nome = nome.strip()
lista = nome.split()

print('Maiuscula: {}\nMinuscula: {}\nQuantidade de letras: {}\nLetras do primeiro nome: {}'.format(nome.upper(), nome.lower(), len("".join(lista)), len(lista[0])))
