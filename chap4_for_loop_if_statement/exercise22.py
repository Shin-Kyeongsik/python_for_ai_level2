import random

n_data = 10
data = [random.randint(-10, 10) for _ in range(n_data)]
print(data)

relu_values = []
for data_ in data:
    if data_ >= 0:
        relu_values.append(data_)
    else:
        relu_values.append(0)
print(relu_values)