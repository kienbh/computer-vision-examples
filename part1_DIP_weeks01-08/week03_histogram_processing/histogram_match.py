import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ---------- Synthetic target PDFs ----------
def synthetic_target_pmf(kind="uniform", mu=128.0, sigma=40.0):
    """
    Tạo PMF mục tiêu (256 mức xám) để dùng làm 'reference' ảo.
    kind: "uniform" hoặc "gaussian"
    mu, sigma: tham số cho gaussian (tính trên thang 0..255)
    """
    x = np.arange(256, dtype=np.float64)
    if kind.lower() == "uniform":
        pmf = np.ones_like(x)
    elif kind.lower() == "gaussian":
        # Gaussian không chuẩn hóa sẵn, cần chuẩn hóa về tổng = 1
        pmf = np.exp(-0.5 * ((x - mu) / float(sigma))**2)
    else:
        raise ValueError("kind phải là 'uniform' hoặc 'gaussian'")
    pmf /= pmf.sum()  # chuẩn hóa thành phân bố rời rạc hợp lệ
    return pmf

# ---------- Histogram Matching to target PMF ----------
def histogram_matching_to_pmf(source_gray_uint8, target_pmf):
    """
    Ánh xạ histogram của ảnh nguồn (grayscale uint8) sao cho PMF đầu ra
    tiệm cận target_pmf (độ dài 256).
    """
    # PMF ảnh nguồn
    h_src, _ = np.histogram(source_gray_uint8.ravel(), bins=256, range=(0, 256))
    pmf_src = h_src.astype(np.float64) / h_src.sum()

    # CDF nguồn & CDF đích (synthetic)
    cdf_src = pmf_src.cumsum()
    cdf_tgt = target_pmf.cumsum()

    # LUT: với mỗi r, tìm s sao cho CDF_tgt(s) ≈ CDF_src(r)
    levels = np.arange(256)
    lut = np.interp(cdf_src, cdf_tgt, levels).round().astype(np.uint8)

    # Ánh xạ ảnh
    matched = lut[source_gray_uint8]
    return matched

# ---------- Plot: giữ nguyên form & trục ----------
def plot_histograms_match_synthetic(source_path, kind="uniform", mu=128, sigma=40):
    """
    So sánh ảnh gốc và ảnh sau Histogram Matching theo synthetic target (uniform/gaussian).
    Histogram dùng fraction of pixels, x-axis 0–255 (hiển thị 0–300), cùng thang y.
    """
    # Đọc ảnh (grayscale)
    src = np.asarray(Image.open(source_path).convert("L"))

    # Tạo PMF đích & matching
    tgt_pmf = synthetic_target_pmf(kind=kind, mu=mu, sigma=sigma)
    matched = histogram_matching_to_pmf(src, tgt_pmf)

    # Histogram (fraction)
    h_src, bins = np.histogram(src,     bins=256, range=(0, 256))
    h_mat, _    = np.histogram(matched, bins=256, range=(0, 256))
    p_src = h_src / h_src.sum()
    p_mat = h_mat / h_mat.sum()

    x = bins[:-1]                      # 0..255
    y_max = max(p_src.max(), p_mat.max()) * 1.10

    fig, axes = plt.subplots(2, 2, figsize=(11, 6))

    # Ảnh gốc
    axes[0, 0].imshow(src, cmap="gray", vmin=0, vmax=255)
    axes[0, 0].set_title("Ảnh gốc (Source)")
    axes[0, 0].axis("off")

    # Histogram gốc (fraction)
    axes[0, 1].bar(x, p_src, width=1.0, color="orange", alpha=0.75)
    axes[0, 1].set_xlim(0, 300)
    axes[0, 1].set_ylim(0, y_max)
    axes[0, 1].set_title("Histogram gốc – Fraction of pixels")
    axes[0, 1].set_xlabel("Gray value (0–255)  |  shown: 0–300")
    axes[0, 1].set_ylabel("Fraction of pixels (nₖ / n)")
    axes[0, 1].grid(alpha=0.3)

    # Ảnh sau Histogram Matching (synthetic target)
    title_tgt = f"Uniform" if kind.lower()=="uniform" else f"Gaussian (μ={mu}, σ={sigma})"
    axes[1, 0].imshow(matched, cmap="gray", vmin=0, vmax=255)
    axes[1, 0].set_title(f"Ảnh sau Histogram Matching – Target: {title_tgt}")
    axes[1, 0].axis("off")

    # Histogram sau matching (fraction) – cùng axis/label
    axes[1, 1].bar(x, p_mat, width=1.0, color="green", alpha=0.75)
    axes[1, 1].set_xlim(0, 300)
    axes[1, 1].set_ylim(0, y_max)
    axes[1, 1].set_title("Histogram sau matching – Fraction of pixels")
    axes[1, 1].set_xlabel("Gray value (0–255)  |  shown: 0–300")
    axes[1, 1].set_ylabel("Fraction of pixels (nₖ / n)")
    axes[1, 1].grid(alpha=0.3)

    plt.suptitle("Histogram Matching với Synthetic Reference", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.show()

# ===== CÁCH DÙNG =====
# 1) Matching về phân bố đều (Uniform):
plot_histograms_match_synthetic("input/Picture2.jpg", kind="uniform")

# 2) Matching về phân bố Gaussian (chọn μ, σ theo ảnh tham chiếu mong muốn):
plot_histograms_match_synthetic("input/Picture2.jpg", kind="gaussian", mu=140, sigma=35)
