import numpy as np
from scipy.optimize import linprog

# 1) profit coefficients (a1,a2,a3,b1,b2,b3)
c = np.array([2.5, -0.5, 1.5, 1.5, -1.5, 0.5])
c_min = -c   # لأن linprog كيدير min

# 2) contraintes A_ub x <= b_ub
A_ub = np.array([
    [1, 0, 0, 1, 0, 0],   # dispo constituant 1
    [0, 1, 0, 0, 1, 0],   # dispo constituant 2
    [0, 0, 1, 0, 0, 1],   # dispo constituant 3
    [4, -6, 4, 0, 0, 0],  # 6a2 >= 4a1 + 4a3
    [7, -3, -3, 0, 0, 0], # 7a1 <= 3a2 + 3a3
    [-1, -1, 1, 0, 0, 0], # a3 <= a1 + a2
    [0, 0, 0, 1, -9, 1],  # 9b2 >= b1 + b3
    [0, 0, 0, 1, -1, -1]  # b1 <= b2 + b3
])

b_ub = np.array([3000, 2000, 4000, 0, 0, 0, 0, 0])

# 3) bornes des variables (x_i >= 0)
bounds = [(0, None)] * 6

# 4) résolution
res = linprog(c_min, A_ub=A_ub, b_ub=b_ub,
              bounds=bounds, method="highs")

print("Success:", res.success)
print(f"Profit optimal =, {-res.fun:.2f} DH")

a1, a2, a3, b1, b2, b3 = res.x
print(f"a1={a1:.2f}, a2={a2:.2f}, a3={a3:.2f}")
print(f"b1={b1:.2f}, b2={b2:.2f}, b3={b3:.2f}")

QA = (a1 + a2 + a3)
QB = (b1 + b2 + b3)
print(f"QA = {QA:.2f}, QB = {QB:.2f}")
print(f"pourcentages A : {a1/QA:.2f}, {a2/QA:.2f}, {a3/QA:.2f}")
print(f"pourcentages B : {b1/QB:.2f}, {b2/QB:.2f}, {b3/QB:.2f}")
