num_quarter = int(input('Enter the number of the quarter of the coordinate plane: '))

if num_quarter == 1:
    print('0 < x < +∞')
    print('0 < y < +∞')
elif num_quarter == 2:
    print('0 < x < -∞')
    print('0 < y < +∞')
elif num_quarter == 3:
    print('0 < x < -∞')
    print('0 < y < -∞')
elif num_quarter == 4:
    print('0 < x < +∞')
    print('0 < y < -∞')
