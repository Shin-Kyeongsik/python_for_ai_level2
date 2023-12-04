import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

scores_ = scores.copy()
scores_sort = []
for _ in range(n_students):
    min_score, min_score_idx = None, None
    for score_idx, score in enumerate(scores_):
        if min_score == None or score < min_score:
            min_score = score
            min_score_idx = score_idx

    scores_sort.append(min_score)
    scores_.pop(min_score_idx)

print(scores_sort)
