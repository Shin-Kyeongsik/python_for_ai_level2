import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

score_dict = {
    'pass_scores': [score for score in scores if score >= threshold],
    'no_pass_scores': [score for score in scores if score < threshold]
}

score_dict['pass_mean'] = sum(score_dict['pass_scores']) / len(score_dict['pass_scores'])
score_dict['no_pass_mean'] = sum(score_dict['no_pass_scores']) / len(score_dict['no_pass_scores'])
print(f"pass mean: {score_dict['pass_mean']:.2f}")
print(f"no pass mean: {score_dict['no_pass_mean']:.2f}")