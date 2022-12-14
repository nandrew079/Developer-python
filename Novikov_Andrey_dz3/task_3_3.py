entered_str = input('Enter string: ')

list_substring = entered_str.split('o')
if len(list_substring) > 2:
    list_substring[1] = list_substring[1][::-1]
    print('o'.join(list_substring))
else:
    print('the letter "o" is one or does not occur')
