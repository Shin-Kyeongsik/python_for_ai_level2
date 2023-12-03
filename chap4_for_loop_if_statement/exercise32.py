import random

n_data = 100
data = [random.randint(0, 100) for _ in range(n_data)]
print(data, '\n')

even_data = [value for value in data if value % 2 == 0]
odd_data = [value for value in data if value % 2 != 0]
print(f"{even_data = }")
print(f"{odd_data = }")