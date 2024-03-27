check_str = input('Enter your text: ')
result = check_str == check_str[:: -1]
if result:
    print(f'{check_str} is polindrome')
else:
    print(f'{check_str} is not polindrome')




