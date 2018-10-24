largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura

print('Serão necessários {:.1f} l litros de tinta'.format(area/2))

#Utilizado para calcular quantos baldes são necessários
#if area % 2 == 0:
#    print('Serão utilizados {:.0f} baldes de tinta'.format(area // 2))
#else:
#    print('Serão utilizados {:.0f} baldes de tinta'.format((area // 2)+1))