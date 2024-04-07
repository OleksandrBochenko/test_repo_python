roles = {
    'admin': ['Alex'],
    'maintainer': ['Sergey'],
    'manager': ['Oleg'],
    'developer': ['Anton']
}
name = input('Enter your name')

for role, users in roles.items():
    if name in users:
        print(f'Hello {role} ')
        break
else:
    print('Hello Guest')

