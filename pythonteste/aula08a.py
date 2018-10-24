from math import sqrt, ceil, floor
import emoji
num = float(input('Digite um número: '))
raiz = sqrt(num)
print('Raiz: {}\nCima: {}\nBaixo: {}'.format(raiz,ceil(raiz),floor(raiz)))