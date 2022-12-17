from random import randint

list_num = [randint(0, 100) for i in range(5)]
print(list_num)
sum_num = 0
for i in range(len(list_num)):
    if i % 2 == 1:
        sum_num += list_num[i]
print(sum_num)
