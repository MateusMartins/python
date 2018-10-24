dia = int(input('Quantidade de dias: '))
km = float(input('Quantidade de quilometros percorridos: '))
print('O valor total a pagar pelo aluguel do carro é: R${:.2f}'.format(float(dia)*60+km*0.15))
