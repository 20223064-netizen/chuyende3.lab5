import numpy as np

# Ma trận điểm (dùng lại từ bài 1)
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("=== BÀI 2: CHUẨN HÓA DỮ LIỆU BẰNG BROADCASTING (Z-SCORE) ===\n")

# 1. Vector trung bình từng môn
mean_col = np.mean(scores, axis=0)
print("1. Vector trung bình từng môn:", mean_col)

# 2. Vector độ lệch chuẩn từng môn
std_col = np.std(scores, axis=0)
print("2. Vector độ lệch chuẩn từng môn:", std_col, "\n")

# 3. Chuẩn hóa toàn bộ ma trận bằng Z-score
z_scores = (scores - mean_col) / std_col

# 4. Làm tròn 2 chữ số
z_round = np.round(z_scores, 2)
print("3-4. Ma trận sau chuẩn hóa (Z-score, làm tròn 2 chữ số):\n")
print(z_round, "\n")

# 5. Kiểm tra trung bình cột sau chuẩn hóa
mean_after = np.mean(z_scores, axis=0)
print("5. Trung bình từng cột sau chuẩn hóa (gần bằng 0):")
print(mean_after, "\n")

# -----------------------
# YÊU CẦU MỞ RỘNG: Min-Max Scaling về [0, 1]
# -----------------------

min_col = np.min(scores, axis=0)
max_col = np.max(scores, axis=0)

minmax_scaled = (scores - min_col) / (max_col - min_col)

print("=== MỞ RỘNG: CHUẨN HÓA MIN-MAX VỀ [0,1] ===\n")
print("Ma trận sau chuẩn hóa Min-Max:\n")
print(np.round(minmax_scaled, 2))
