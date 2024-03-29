number = int(input('Enter your number: '))
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for element in numbers_list:
    if element % number == 0:
        result.append(element)
print(f'Numbers that not divided by {number} are {result}')







