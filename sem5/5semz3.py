
def reverse(n):
    if n <= 0:
        return '+'
    num = input('ВВеди число')
    return reverse(n-1) + ' '+ num
print(reverse(4))

n = int(input('Введите число n: ')) 