'''
Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.
'''
a = int (input('Введите длинну шоколадки в дольках: '))
b = int (input('Введите ширину шоколадки в дольках: '))
c = int (input('Введите отделяемое количество долек: '))

if (a * b) > c and c % a == 0 or (a * b) > c and c % b == 0:
    print('yes')
else: print ('no')
