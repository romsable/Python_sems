# ввод: st = '8 5 77 -14 101 45'

# вывод: 77 -14 45

st = "8 5 77 -14 101 45"
numbers = [int(i) for i in st.split() if 10 <= abs(int(i)) < 100]
print(numbers)
