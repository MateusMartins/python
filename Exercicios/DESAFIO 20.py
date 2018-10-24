import random

aluno = []
i = 1
while i <= 4:
    aluno.append(input('Nome do aluno: '))
    i += 1

random.shuffle(aluno)

print('\nOrdem de apresentação')
j = 0
while j < 4:
    print('{}º: {}'.format(j+1, aluno[j]))
    j += 1
