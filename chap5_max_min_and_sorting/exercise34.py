import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

max_score = 0
for score in scores:
    if score > max_score:
        max_score = score

print(f"{max_score = }")