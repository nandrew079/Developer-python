num_day = int(input('Enter the day of the week as a number: '))

if num_day == 6 or num_day == 7:
    print('yes')
elif not (1 <= num_day <= 7):
    print('error')
else:
    print('no')
