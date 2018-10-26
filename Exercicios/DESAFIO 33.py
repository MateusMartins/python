number1 = float(input('Número: '))
number2 = float(input('Número: '))
number3 = float(input('Número: '))

maior = 0
if number1 > number2 and number1 > number3:
    maior = number1
    if number2 > number3:
        menor = number3
    else:
        menor = number2

elif number2 > number1 and number2 > number3:
    maior = number2
    if number1 > number3:
        menor = number3
    else:
        menor = number1

else:
    maior = number3
    if number1 > number2:
        menor = number2
    else:
        menor = number1

print('Maior: {}\nMenor: {}'.format(maior, menor))