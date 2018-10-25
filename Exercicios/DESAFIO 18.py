from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
