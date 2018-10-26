distance = float(input('Distancia(Km): '))
if distance <= 200:
    print('R${:.2f}'.format(distance*0.5))
else:
    print('R${:.2f}'.format(distance * 0.45))
