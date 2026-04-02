import numpy as np
import matplotlib.pyplot as plt

# 1. Tạo 100 bước ngẫu nhiên (+1 hoặc -1)
np.random.seed(0)  # để kết quả tái lập (có thể bỏ)
steps = np.random.choice([-1, 1], size=100)

# 2. Tính vị trí sau mỗi bước (bắt đầu từ vị trí 0)
positions = np.cumsum(steps)

# 3. In 10 giá trị đầu tiên của dãy vị trí
print("10 vị trí đầu tiên:")
print(positions[:10])

# 4. Vẽ đồ thị Random Walk
plt.figure(figsize=(10,5))
plt.plot(positions, marker='o')
plt.title("Random Walk - 100 bước")
plt.xlabel("Bước")
plt.ylabel("Vị trí")
plt.grid(True)
plt.show()

# 5. Thống kê thêm
final_pos = positions[-1]
max_pos = np.max(positions)
min_pos = np.min(positions)

print("\nVị trí cuối cùng:", final_pos)
print("Vị trí lớn nhất:", max_pos)
print("Vị trí nhỏ nhất:", min_pos)
