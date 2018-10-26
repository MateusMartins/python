year = int(input('Ano: '))

if year % 4 == 0 and year % 100 != 0:
    print('É bissexto')
elif year % 100 == 0 and year % 400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')
