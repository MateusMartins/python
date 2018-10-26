number = int(input('Número: '))

def pairOdd(x):
    if x % 2 == 0:
        return 'Par'
    else:
        return 'Impar'

print(pairOdd(number))
