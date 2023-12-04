import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

score_dict = {key: 0 for key in ['pass_sum', 'no_pass_sum',
                                 'pass_cnt', 'no_pass_cnt']}
for score in scores:
    if score >= threshold:
        score_dict['pass_sum'] += score
        score_dict['pass_cnt'] += 1
    else:
        score_dict['no_pass_sum'] += score
        score_dict['no_pass_cnt'] += 1

score_dict['pass_mean'] = score_dict['pass_sum'] / score_dict['pass_cnt']
score_dict['no_pass_mean'] = score_dict['no_pass_sum'] / score_dict['no_pass_cnt']
print(f"pass mean: {score_dict['pass_mean']:.2f}")
print(f"no pass mean: {score_dict['no_pass_mean']:.2f}")
