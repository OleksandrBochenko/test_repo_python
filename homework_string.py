my_str = input("Enter you text: ")
text_to_delete = input("Enter text you want to delete: ")
result = my_str.replace(text_to_delete, "")
print(f'Result is {result}')