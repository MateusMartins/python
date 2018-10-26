distance = float(input('Distancia(Km): '))
if distance <= 200:
    print('R${}'.format(distance*0.5))
else:
    print('R${}'.format(distance * 0.45))
