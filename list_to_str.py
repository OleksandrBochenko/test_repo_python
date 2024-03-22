my_list = ['Hillel', 'AQA', 'TEST']
my_str = '//'.join(my_list)
print(f"'Hillel', 'AQA', 'TEST': {my_str}")
new_list = my_str.split('//')
print(f"'Hillel', 'AQA', 'TEST': {new_list}")
