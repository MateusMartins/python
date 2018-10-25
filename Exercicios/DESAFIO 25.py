nome = input('Digite o seu nome completo: ')
dividido = nome.split()

i = 0
while len(dividido) > i:
    if dividido[i] == 'Silva':
        resultado = 'Tem Silva'
        break
    else:
        resultado = 'Não tem silva'
    i += 1

print(resultado)
