frase = input('Insira uma frase: ').strip().lower()

print('Quantidade de "a": {}\nPrimeira ocorrência: {}\nUltima ocorrência: {}'.format(frase.count('a'),frase.find('a')+1,frase.rfind('a')+1))
