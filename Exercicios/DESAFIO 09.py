number = int(input('Insira um número: '))
print('-'*12)
i = 1
while i <= 10:
    print('{} x {:2} = {}'.format(number, i, i * number))
    i += 1
print('-'*12)
