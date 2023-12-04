import random

n_students = 10
scores = [random.randint(0, 120) for _ in range(n_students)]
print(scores)

max_score, max_score_idx = None, None
for score_idx, score in enumerate(scores):
    if max_score == None or score > max_score:
        max_score = score
        max_score_idx = score_idx

print(f"max / max idx: {max_score} / {max_score_idx}")