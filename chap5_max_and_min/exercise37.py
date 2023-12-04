import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

min_score = None
for score in scores:
    if min_score == None or score < min_score:
        min_score = score

print(f"{min_score = }")