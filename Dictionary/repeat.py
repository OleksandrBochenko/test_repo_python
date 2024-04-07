my_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
my_dict = {}
for letter in my_link:
    if letter not in my_dict:
        my_dict[letter] = my_link.count(letter)

print(my_dict)
