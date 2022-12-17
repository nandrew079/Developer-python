from random import randint

a = int(input('Enter A: '))
b = int(input('Enter B: '))

matrix = []
for i in range(a):
    s_list = [randint(0, 100) for j in range(b)]
    matrix.append(s_list)
    print(s_list)

for s_list in matrix:
    sum_num = 0
    for num in s_list:
        sum_num += num
    print(sum_num / b)
