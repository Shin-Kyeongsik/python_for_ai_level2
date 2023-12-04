keys = ['a', 'b', 'c', 'd', 'e']
values = [i for i in range(5)]
print(keys)
print(values, '\n')

test_dict = {key: value for key, value in zip(keys, values)}
print(test_dict)