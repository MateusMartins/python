largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
if area % 2 == 0:
    print('Serão utilizados {:.0f} baldes de tinta'.format(area // 2))
else:
    print('Serão utilizados {:.0f} baldes de tinta'.format((area // 2)+1))