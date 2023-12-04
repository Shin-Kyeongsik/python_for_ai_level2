import random

n_students = 100
scores = [random.randint(0, 100) for _ in range(n_students)]

score_idx = 0
while True:
    user_input = input("q[quit], n[next]: ")
    if user_input == 'q':
        break
    elif user_input == 'n':
        score = scores[score_idx]
        print(f"{score_idx}-th score: {score}")
        score_idx += 1