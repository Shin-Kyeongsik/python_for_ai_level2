import random

n_students = 20
scores = [random.randint(0, 100) for _ in range(n_students)]
print(scores)

max_min_dict = {'max': None, 'max_idx': None, 'min': None, 'min_idx': None}
for score_idx, score in enumerate(scores):
    if max_min_dict['max'] == None or score > max_min_dict['max']:
        max_min_dict['max'] = score
        max_min_dict['max_idx'] = score_idx

    if max_min_dict['min'] == None or score < max_min_dict['min']:
        max_min_dict['min'] = score
        max_min_dict['min_idx'] = score_idx

print(max_min_dict)