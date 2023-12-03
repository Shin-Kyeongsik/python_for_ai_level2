import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

scores_pass = []
for score in scores:
    if score >= threshold:
        scores_pass.append(score)
print(f"pass scores: {scores_pass}")