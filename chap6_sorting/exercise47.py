import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

pass_scores = []
for score in scores:
    if score < threshold:
        continue

    pass_scores.append(score)
print(pass_scores)