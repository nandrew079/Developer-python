from random import randint

num_list = [randint(0, 100) for i in range(30)]
print(num_list)

for i in range(len(num_list)):
        min_num = i

        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_num]:
                min_num = j

        num_list[i], num_list[min_num] = num_list[min_num], num_list[i]

print(num_list)
