import random

n_students = 10
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

sort_indices = []
for _ in range(n_students):
    min_score, min_score_idx = None, None
    for score_idx, score in enumerate(scores):
        if score_idx in sort_indices:
            continue

        if min_score == None or score < min_score:
            min_score = score
            min_score_idx = score_idx
    sort_indices.append(min_score_idx)
print(sort_indices)