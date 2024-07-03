# ; Напишите программу, которая принимает на вход
# ; строку, и отслеживает, сколько раз каждый символ
# ; уже встречался. Количество повторов добавляется к
# ; символам с помощью постфикса формата _n.
# ; Input: a a a b c a a d c d d
# ; Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# ; Для решения данной задачи используйте функцию
# ; .split()

# input = 'a a a b c a a d c d d'
# input = input.split()
# print(input)
# new_str = ''
# count  = 1

# for i in input:
#     if i*1 in input:
#         new_str += i

    
# print(new_str)

# dict = {}
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split():
#     count = dict.get(i)
#     if count != None:
#         string_res = string_res + i + "_" + str(count) + " "
#         dict[i] = count + 1
#     else:
#         dict[i] = 1
#         string_res = string_res + i + " "

# print(string_res)


dict = {}
string = "a a a b c a a d c d d"
string_res = ""

for i in string.split():
    if i in dict:
        string_res = string_res + i + "_" + str(dict[i]) + " "
        print(string_res)
    else:
        string_res = string_res + i + " "
    dict[i] = 1 + dict.get(i, 0)
    print(dict)
    print(string_res)
print(string_res)