import random

n_students = 20
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

scores_pass, scores_no_pass = [], []
for score in scores:
    if score >= threshold:
        scores_pass.append(score)
    else:
        scores_no_pass.append(score)

mean_pass = sum(scores_pass) / len(scores_pass)
mean_no_pass = sum(scores_no_pass) / len(scores_no_pass)
print(f"{mean_pass = :.2f}")
print(f"{mean_no_pass = :.2f}")