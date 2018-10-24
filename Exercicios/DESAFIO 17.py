from math import hypot

co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
print('Valor da hipotenusa: {:.2f}cm'.format(hypot(co, ca)))
