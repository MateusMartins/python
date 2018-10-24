import random
aluno = []
i = 1
while i<=4:
    aluno.append(input('Nome do aluno: '))
    i += 1

print('O aluno escolhido foi: {}'.format(random.choice(aluno)))
