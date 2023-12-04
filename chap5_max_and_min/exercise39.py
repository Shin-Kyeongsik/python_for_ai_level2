import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

min_score, min_score_idx = None, None
for score_idx, score in enumerate(scores):
    if min_score == None or score < min_score:
        min_score = score
        min_score_idx = score_idx

print(f"min / min idx: {min_score} / {min_score_idx}")