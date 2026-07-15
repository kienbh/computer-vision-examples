import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ====== HÀM: Histogram Equalization ======
def histogram_equalization(img_gray):
    flat = img_gray.ravel()
    hist = np.bincount(flat, minlength=256)
    cdf = hist.cumsum()
    cdf_norm = (cdf - cdf.min()) / (cdf.max() - cdf.min())
    lut = np.floor(255 * cdf_norm + 0.5).astype(np.uint8)
    return lut[flat].reshape(img_gray.shape)

# ====== HÀM: Vẽ biểu đồ so sánh dạng cột ======
def plot_histograms_compare(image_path):
    # --- Đọc ảnh & chuyển sang grayscale ---
    img = Image.open(image_path).convert("L")
    img = np.asarray(img)

    # --- Cân bằng histogram ---
    img_eq = histogram_equalization(img)

    # --- Tính histogram (256 bins) & chuẩn hóa về fraction of pixels ---
    h_orig, bins = np.histogram(img, bins=256, range=(0, 256))
    h_eq, _ = np.histogram(img_eq, bins=256, range=(0, 256))
    p_orig = h_orig / h_orig.sum()
    p_eq = h_eq / h_eq.sum()

    # --- Chuẩn bị trục x và giới hạn y ---
    x = bins[:-1]
    y_max = max(p_orig.max(), p_eq.max()) * 1.1

    # --- VẼ ---
    fig, axes = plt.subplots(2, 2, figsize=(11, 6))

    # Ảnh gốc
    axes[0, 0].imshow(img, cmap='gray', vmin=0, vmax=255)
    axes[0, 0].set_title("Ảnh gốc (Original Image)")
    axes[0, 0].axis("off")

    # Histogram gốc
    axes[0, 1].bar(x, p_orig, width=1.0, color="orange", alpha=0.7)
    axes[0, 1].set_xlim(0, 300)
    axes[0, 1].set_ylim(0, y_max)
    axes[0, 1].set_title("Histogram gốc – Fraction of pixels")
    axes[0, 1].set_xlabel("Gray value (0–255)")
    axes[0, 1].set_ylabel("Fraction of pixels (nₖ / n)")
    axes[0, 1].grid(alpha=0.3)

    # Ảnh sau equalization
    axes[1, 0].imshow(img_eq, cmap='gray', vmin=0, vmax=255)
    axes[1, 0].set_title("Ảnh sau cân bằng Histogram (Equalized Image)")
    axes[1, 0].axis("off")

    # Histogram sau equalization
    axes[1, 1].bar(x, p_eq, width=1.0, color="green", alpha=0.7)
    axes[1, 1].set_xlim(0, 300)
    axes[1, 1].set_ylim(0, y_max)
    axes[1, 1].set_title("Histogram sau cân bằng – Fraction of pixels")
    axes[1, 1].set_xlabel("Gray value (0–255)")
    axes[1, 1].set_ylabel("Fraction of pixels (nₖ / n)")
    axes[1, 1].grid(alpha=0.3)

    plt.suptitle("So sánh Histogram của ảnh gốc và ảnh sau cân bằng", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()

# ====== CÁCH DÙNG ======
plot_histograms_compare("input/Fig0316(1)(top_left).tif")
