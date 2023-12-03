import random

n_data = 100
preds = [random.randint(0, 1) for _ in range(n_data)]
labels = [random.randint(0, 1) for _ in range(n_data)]
print(f"{preds = }")
print(f"{labels = }\n")

n_corrects = 0
for pred, label in zip(preds, labels):
    if pred == label:
        n_corrects += 1
acc = n_corrects / n_data
print(f"{acc = :.2f}")