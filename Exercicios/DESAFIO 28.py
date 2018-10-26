from random import choice

numbers = [0, 1, 2, 3, 4, 5]

choiced = choice(numbers)

print('Eu já escolhi um número, será que você consegue adivinhar?')

option = int(input('Selecione um número entre 0 e 5: '))

if choiced == option:
    print('Você acertou!')
else:
    print('Você errou')
