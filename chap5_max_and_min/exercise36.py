import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

max_score = None
for score in scores:
    if max_score == None or score > max_score:
        max_score = score

print(f"{max_score = }")