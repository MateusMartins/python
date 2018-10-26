a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if (b - c) < a and a < (b + c) and (a - c) < b and b < (a + c) and (a - b) < c and c < (a + b):
    print('É um triângulo')
else:
    print('Não é um triângulo')
