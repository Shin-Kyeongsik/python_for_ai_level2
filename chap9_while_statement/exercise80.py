import random

n_students = 10000
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

threshold = 80
pass_students = []
score_idx = 0
while len(pass_students) <= 10:
    score = scores[0]
    if score >= threshold:
        pass_students.append(score_idx)

    scores.pop(0)
    score_idx += 1
print(pass_students)