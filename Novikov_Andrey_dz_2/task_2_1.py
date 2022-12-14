x = int(input('Enter number x: '))
y = int(input('Enter number y: '))

print('result')
for i in range(x, y+1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
