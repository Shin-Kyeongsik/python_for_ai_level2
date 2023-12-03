import random

n_data = 100
preds = [random.randint(0, 1) for _ in range(n_data)]
labels = [random.randint(0, 1) for _ in range(n_data)]
print(f"{preds = }")
print(f"{labels = }\n")

n_TP, n_TN = 0, 0
n_FP, n_FN = 0, 0
for pred, label in zip(preds, labels):
    if pred == label:
        if pred == 1: n_TP += 1
        else: n_TN += 1
    else:
        if pred == 1: n_FP += 1
        else: n_FN += 1

print(f"{n_TP = } | {n_FP = }")
print("---------------------")
print(f"{n_FN = } | {n_TN = }")