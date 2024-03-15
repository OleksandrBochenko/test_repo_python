number_1 = float(input(' enter first number '))
number_2 = float(input(' enter second number '))
operation = input('Enter operation (+,-,*,/): ')
if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    result = number_1 / number_2
else:
    result = 'Invalid operation'

print(result)
