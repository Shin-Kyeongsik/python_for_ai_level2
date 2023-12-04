import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

scores_ = scores.copy()
scores_sort = []

max_score, max_score_idx = None, None
for score_idx, score in enumerate(scores_):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx

scores_sort.append(max_score)
scores_.pop(max_score_idx)

print(f"{scores_sort = }")
print(f"{scores_ = }")