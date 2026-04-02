import numpy as np

# Ma trận số lượng bán
quantity = np.array([
    [10, 12, 9, 14],   # Sản phẩm 1
    [5, 7, 8, 6],      # Sản phẩm 2
    [20, 18, 25, 22]   # Sản phẩm 3
])

# Giá mỗi sản phẩm
price = np.array([15000, 25000, 10000])

print("=== BÀI 3: PHÂN TÍCH DOANH THU BẰNG MA TRẬN ===\n")

# 1. Doanh thu từng sản phẩm theo từng ngày
revenue = quantity * price.reshape(3, 1)
print("1. Doanh thu từng sản phẩm theo từng ngày:\n", revenue, "\n")

# 2. Tổng doanh thu từng sản phẩm
sum_product = np.sum(revenue, axis=1)
print("2. Tổng doanh thu từng sản phẩm:\n", sum_product, "\n")

# 3. Tổng doanh thu từng ngày
sum_day = np.sum(revenue, axis=0)
print("3. Tổng doanh thu từng ngày:\n", sum_day, "\n")

# 4. Tìm ngày có doanh thu cao nhất (cộng 1 vì index từ 0)
best_day = np.argmax(sum_day) + 1
print("4. Ngày có doanh thu cao nhất:", best_day, "\n")

# 5. Tỷ trọng doanh thu từng sản phẩm
ratio = sum_product / np.sum(sum_product)
print("5. Tỷ trọng doanh thu từng sản phẩm (%):\n", np.round(ratio * 100, 2), "%")
