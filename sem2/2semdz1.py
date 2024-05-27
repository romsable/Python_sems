n = int (input('введите количество монет: '))
x0 = 0
x1 = 0
for i in range(n):
    x = int (input('Введите значение(0 или 1): '))
    if x == 0:
        x0 += 1
    else: 
        x1 += 1
if x0 < x1:
    print (f"Нужно перевернуть {x0} монет")
else:
    print (f"Нужно перевернуть {x1} монет")