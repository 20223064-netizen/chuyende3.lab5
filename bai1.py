import numpy as np

# Ma trận điểm của 5 sinh viên (4 môn học)
scores = np.array([
    [7.5, 8.0, 6.5, 9.0],
    [6.0, 7.0, 7.5, 8.0],
    [8.5, 9.0, 8.0, 9.5],
    [5.5, 6.0, 6.5, 7.0],
    [9.0, 8.5, 9.5, 8.0]
])

print("=== BÀI 1: THỐNG KÊ MÔ TẢ DỮ LIỆU ĐIỂM SINH VIÊN ===\n")

# 1. In ra ma trận điểm
print("1. Ma trận điểm:")
print(scores, "\n")

# 2. Điểm trung bình toàn bộ ma trận
mean_all = np.mean(scores)
print("2. Điểm trung bình toàn bộ ma trận:", mean_all, "\n")

# 3. Điểm trung bình từng sinh viên
mean_students = np.mean(scores, axis=1)
print("3. Điểm trung bình từng sinh viên:")
for i, avg in enumerate(mean_students, start=1):
    print(f"   - Sinh viên {i}: {avg}")
print()

# 4. Điểm trung bình theo từng môn
mean_subjects = np.mean(scores, axis=0)
print("4. Điểm trung bình từng môn:")
for i, avg in enumerate(mean_subjects, start=1):
    print(f"   - Môn {i}: {avg}")
print()

# 5. Điểm cao nhất và thấp nhất
print("5. Điểm cao nhất trong ma trận:", np.max(scores))
print("   Điểm thấp nhất trong ma trận:", np.min(scores), "\n")

# 6. Độ lệch chuẩn từng môn
std_subjects = np.std(scores, axis=0)
print("6. Độ lệch chuẩn từng môn:")
for i, std in enumerate(std_subjects, start=1):
    print(f"   - Môn {i}: {std}")
print()

# 7. Sinh viên có điểm trung bình cao nhất
best_student = np.argmax(mean_students) + 1   # +1 vì index bắt đầu từ 0
best_score = np.max(mean_students)

print("7. Sinh viên có điểm trung bình cao nhất:")
print(f"   - Sinh viên {best_student} với điểm TB = {best_score}")
