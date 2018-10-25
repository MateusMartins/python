from math import trunc

numero = int(input("Digite um número entre 0 e 9999: "))

milhar = trunc(numero/1000)
centena = trunc((numero % 1000)/100)
dezena = trunc((numero % 100)/10)
unidade = trunc((numero % 10))

print('unidade: {:>}\ndezena: {:>}\ncentena: {:>}\nmilhar: {:>}'.format(unidade, dezena, centena, milhar))

#numero = input("Digite um número entre 0 e 9999: ")

#if len(numero) == 4:
#    milhar = numero[0]
#    centena = numero[1]
#    dezena = numero[2]
#    unidade = numero[3]
#elif len(numero) == 3:
#    milhar = '0'
#    centena = numero[0]
#    dezena = numero[1]
#    unidade = numero[2]
#elif len(numero) == 2:
#    milhar = '0'
#    centena = '0'
#    dezena = numero[0]
#    unidade = numero[1]
#elif len(numero) == 1:
#    milhar = '0'
#    centena = '0'
#    dezena = '0'
#    unidade = numero[0]

#print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(unidade, dezena, centena, milhar))
