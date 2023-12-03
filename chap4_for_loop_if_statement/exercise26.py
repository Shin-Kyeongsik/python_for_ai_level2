import random

vec_dim = 5
u = [random.randint(-5, 5) for _ in range(vec_dim)]
v = [random.randint(-5, 5) for _ in range(vec_dim)]
print(f"{u = }")
print(f"{v = }\n")

manhattan_dist = 0
for u_el, v_el in zip(u, v):
    diff = u_el - v_el
    if diff > 0:
        manhattan_dist += diff
    else:
        manhattan_dist += -diff
print(f"{manhattan_dist = }")