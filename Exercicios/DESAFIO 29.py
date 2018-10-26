speed = float(input('Velocidade: '))

if speed > 80:
    print('Você foi multado! ta na roça!\nVai ter que pagar R${:.2f}'.format((speed-80)*7))
else:
    print('Ta suave')
