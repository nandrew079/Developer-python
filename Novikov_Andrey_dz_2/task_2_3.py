salary = int(input('Enter salary: '))

count_25 = 0
count_10 = 0
count_3 = 0

if salary // 25 > 0:
    count_25 = salary // 25
    salary = salary - count_25 * 25

if salary // 10 > 0:
    count_10 = salary // 10
    salary = salary - count_10 * 10

if salary // 3 > 0:
    count_3 = salary // 3
    salary = salary - count_3 * 3

print(f'result: {count_25} for 25 rubles, {count_10} for 10 rubles, {count_3} for 3 rubles, {salary} for 1 ruble ')
