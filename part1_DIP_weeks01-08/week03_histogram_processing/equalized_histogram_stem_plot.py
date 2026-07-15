import numpy as np
import matplotlib.pyplot as plt

# ===== Dữ liệu từ bảng =====
k = np.arange(8)
z_k = np.array([0, 1/7, 2/7, 3/7, 4/7, 5/7, 6/7, 1.0])
p_out = np.array([0.00, 0.00, 0.00, 0.15, 0.20, 0.30, 0.20, 0.15])

# ===== Vẽ biểu đồ stem =====
plt.figure(figsize=(5.5, 4.5))
(markerline, stemlines, baseline) = plt.stem(k, p_out, basefmt=" ")
plt.setp(markerline, marker='o', markersize=6, markerfacecolor='white', color='blue')
plt.setp(stemlines, color='blue', linewidth=1.5)

# ===== Cấu hình trục và nhãn =====
plt.xlim(0, 8)
plt.ylim(0, 0.35)
plt.xlabel('k (mức xám rời rạc)')
plt.ylabel('p_out(z_k)')
plt.title('Histogram sau cân bằng (stem plot)')
plt.grid(alpha=0.2)
plt.tight_layout()
plt.show()
