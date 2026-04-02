import numpy as np

A = np.array([[2, 1],
              [1, 3]])

B = np.array([[4, 2],
              [1, 5]])

print("A + B:\n", A + B)
print("A - B:\n", A - B)
print("A @ B:\n", A @ B)

detA = np.linalg.det(A)
print("Định thức A:", detA)

invA = np.linalg.inv(A)
print("Ma trận nghịch đảo A:\n", invA)

# Giải hệ phương trình
C = np.array([5, 7])
X = invA @ C
print("Nghiệm hệ phương trình (x, y):", X)
