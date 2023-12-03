import random

n_data = 10
data = [random.randint(-10, 10) for _ in range(n_data)]
print(data)

data_abs = []
for data_ in data:
    if data_ >= 0:
        data_abs.append(data_)
    else:
        data_abs.append(-data_)
print(data_abs)