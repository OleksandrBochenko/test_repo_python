params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
for key, value in params.items():
    initial_str = initial_str + f'{key}={value}&'
print(initial_str.strip('&'))






