course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
user_key = input('Enter your key: ')

try:
    value = course[user_key]
except KeyError:
    print(f'Key is absent in the {course}')
else:
    print(f'Value is {value}')





