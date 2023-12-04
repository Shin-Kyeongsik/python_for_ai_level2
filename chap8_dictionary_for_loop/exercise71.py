import random

n_students = 100
threshold = 80
scores = [random.randint(0, 100) for _ in range(n_students)]

hist_dict = {key: 0 for key in ['0', '20', '40', '60', '80']}
for score in scores:
    bin_idx = score // 20
    if bin_idx == 5:
        bin_idx = 4
    hist_dict[str(bin_idx*20)] += 1

print(hist_dict)