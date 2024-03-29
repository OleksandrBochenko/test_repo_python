my_list = [1, 2, 3, 4, 6, 7, 8]
for element in range(0, len(my_list) - 1):
    if my_list[element] + 1 != my_list[element + 1]:
        print(f'{my_list[element + 1]} is not consecutive')
        break
else:
    print(f'{my_list} is consecutive')
