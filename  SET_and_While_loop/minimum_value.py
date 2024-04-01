elements = [1, 5, 68, 0, -2]
min_value = elements[0]
for element in elements:
    if min_value > element:
        min_value = element
print(f'{min_value} is minimal value')


