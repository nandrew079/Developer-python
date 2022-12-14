str_float_num = input('Enter float number: ')
str_verification = '0123456789.'

result = True
for ch in str_float_num:
    if ch not in str_verification:
        result = False
        break

print(result)
