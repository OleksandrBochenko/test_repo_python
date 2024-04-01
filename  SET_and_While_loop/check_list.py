my_list = [1, 2, 3, 4, 5, 5, 5, 6, 6]
set_1 = set(my_list)
if len(my_list) == len(set_1):
    print(f'list is unique {my_list}')
else:
    print(f'list is not unique {my_list}')