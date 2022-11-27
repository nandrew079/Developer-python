import math

print('Enter the coordinates of the point A:')
xa = float(input('x = '))
ya = float(input('y = '))

print('Enter the coordinates of the point B:')
xb = float(input('x = '))
yb = float(input('y = '))

result = round(math.sqrt((xb - xa)**2 + (yb - ya)**2), 2)
print(result)
