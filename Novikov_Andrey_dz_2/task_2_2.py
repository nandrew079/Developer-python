x = int(input('Enter number x: '))

list_number = []
for i in range(x):
    list_number.append(int(input(f'Number № {i+1}: ')))

list_number.sort()
print(f'result max 1: {list_number.pop()}')
print(f'result max 2: {list_number.pop()}')
