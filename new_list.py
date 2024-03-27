my_list = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
win = my_list[-1][-1][0]
new_list = [win]
print(f'result: {new_list}')