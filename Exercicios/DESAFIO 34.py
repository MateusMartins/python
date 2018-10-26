salary = float(input('Digite seu salário: '))

if salary > 1250:
    newSalary = salary*1.1
else:
    newSalary = salary * 1.15

print('R$:{:.2f}'.format(newSalary))
