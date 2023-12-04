import random

n_students = 20
scores = [random.randint(0, 100) for _ in range(n_students)]

score_mean = sum(scores) / len(scores)
score_var = sum([(score - score_mean)**2 for score in scores]) / len(scores)
score_std = score_var**0.5

max_score, max_score_idx = None, None
min_score, min_score_idx = None, None
for score_idx, score in enumerate(scores):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx

    if min_score == None or score < min_score:
        min_score = score
        min_score_idx = score_idx

score_info = [score_mean, score_var, score_std,
              max_score, max_score_idx,
              min_score, min_score_idx]
print(f"{score_info = }")