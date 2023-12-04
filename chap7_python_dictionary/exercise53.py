import random

n_students = 20
scores = [random.randint(0, 100) for _ in range(n_students)]

score_info = {}

score_info['mean'] = sum(scores) / len(scores)
score_info['var'] = sum([(score - score_info['mean'])**2 for score in scores]) / len(scores)
score_info['std'] = score_info['var']**0.5

max_score, max_score_idx = None, None
min_score, min_score_idx = None, None
for score_idx, score in enumerate(scores):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx

    if min_score == None or score < min_score:
        min_score = score
        min_score_idx = score_idx

score_info['max'] = max_score
score_info['max_idx'] = max_score
score_info['min'] = min_score
score_info['min_idx'] = min_score_idx

print(score_info)