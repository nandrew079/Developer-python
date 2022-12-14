number = input('Enter number: ')

prev = -1
result = True
for i in number:
    if prev > int(i):
        result = False
        break
    prev = int(i)

print(result)
