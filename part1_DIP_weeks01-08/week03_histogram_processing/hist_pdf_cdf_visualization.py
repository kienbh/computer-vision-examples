# ============================================
# Computer Vision · Week 03
# Histogram, PDF, and CDF Visualization
# Author: Bùi Huy Kiên
# ============================================

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# =====================================================
# Hàm vẽ chung: Histogram + PDF + CDF + Threshold
# =====================================================
def plot_hist_pdf_cdf(
    data_01,
    title="Histogram – PDF – CDF",
    xlabel="Giá trị (chuẩn hóa [0,1])",
    threshold=None,
    bins=30,
    color_hist="#F4A261",  # màu cam nhạt
    color_pdf="#1f77b4",   # xanh lam
    color_cdf="#C71585",   # tím/đỏ hồng
    save_path=None
):
    """Vẽ Histogram, PDF và CDF trên cùng một đồ thị"""
    data_01 = np.asarray(data_01).ravel()
    data_01 = np.clip(data_01, 0, 1)

    # Histogram (density=True để chuẩn hóa)
    hist, bin_edges = np.histogram(data_01, bins=bins, range=(0,1), density=True)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    bin_width = bin_edges[1] - bin_edges[0]

    # PDF (đường cong mượt)
    pdf_est = np.convolve(hist, np.ones(3)/3, mode="same")

    # CDF (tích lũy)
    cdf_est = np.cumsum(pdf_est) * bin_width
    cdf_est = np.clip(cdf_est, 0, 1)

    # Bắt đầu vẽ
    fig, ax1 = plt.subplots(figsize=(8,4.2))

    # Histogram
    ax1.hist(
        data_01, bins=bins, range=(0,1), density=True,
        color=color_hist, alpha=0.6, label="Histogram (chuẩn hóa)"
    )

    # PDF
    ax1.plot(bin_centers, pdf_est, color=color_pdf, linewidth=2, label="PDF (mật độ)")
    ax1.scatter(bin_centers, pdf_est, color=color_pdf, s=12)

    ax1.set_xlabel(xlabel)
    ax1.set_ylabel("PDF (mật độ)")
    ax1.grid(alpha=0.3)
    ax1.set_xlim(0,1)

    # CDF (trục phụ)
    ax2 = ax1.twinx()
    ax2.plot(bin_centers, cdf_est, color=color_cdf, linestyle="--", linewidth=2, label="CDF (tích lũy)")
    ax2.set_ylabel("CDF")
    ax2.set_ylim(0,1.05)

    # Threshold (nếu có)
    if threshold is not None:
        thr = float(np.clip(threshold,0,1))
        ax1.axvline(thr, color="#8B0000", linestyle="--", linewidth=2, label=f"Threshold = {thr:.2f}")
        idx = (np.abs(bin_centers - thr)).argmin()
        cprob = cdf_est[idx]
        ax2.hlines(cprob, xmin=thr, xmax=1, colors="#444444", linestyles=":", linewidth=1.5)
        ax2.annotate(f"CDF={cprob:.2f}", xy=(thr,cprob), xytext=(thr+0.03, min(1,cprob+0.1)),
                     arrowprops=dict(arrowstyle="->", color="#444444"), fontsize=9)

    # Gộp legend
    h1,l1 = ax1.get_legend_handles_labels()
    h2,l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc="upper left", frameon=True)

    plt.title(title)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=200)
    plt.show()


# =====================================================
# Hàm Equalization
# =====================================================
def equalize_gray_image_np(img_gray_uint8):
    """Equalize histogram ảnh xám bằng NumPy."""
    flat = img_gray_uint8.ravel()
    hist = np.bincount(flat, minlength=256).astype(np.float64)
    cdf = hist.cumsum()
    cdf_norm = (cdf - cdf.min()) / (cdf.max() - cdf.min())  # [0,1]
    lut = np.floor(255 * cdf_norm + 0.5).astype(np.uint8)
    out = lut[flat].reshape(img_gray_uint8.shape)
    return out


# =====================================================
# Hàm phân tích ảnh gốc (Histogram + PDF + CDF)
# =====================================================
def analyze_gray_image(image_path, title_prefix="Original", threshold=None, bins=32):
    """Vẽ Histogram + PDF + CDF cho 1 ảnh xám."""
    img = Image.open(image_path).convert("L")
    arr = np.asarray(img)
    data_01 = arr.astype(np.float32) / 255.0
    plot_hist_pdf_cdf(
        data_01,
        title=f"{title_prefix}: Histogram + PDF + CDF",
        xlabel="Mức xám chuẩn hóa (0–1)",
        threshold=threshold,
        bins=bins,
        save_path=f"{title_prefix.lower().replace(' ','_')}_hist_pdf_cdf.png"
    )
    return arr


# =====================================================
# TASK 2: Ảnh trước & sau Equalization
# =====================================================
def analyze_before_after_equalization(image_path, threshold=None, bins=32):
    """
    Task 2: Vẽ 2 biểu đồ – ảnh gốc và ảnh sau Equalization.
    Kết quả gồm:
        - Original_hist_pdf_cdf.png
        - image_equalized.png
        - Equalized_hist_pdf_cdf.png
    """
    # 1️⃣ Ảnh gốc
    orig = analyze_gray_image(image_path, title_prefix="Original", threshold=threshold, bins=bins)

    # 2️⃣ Equalization
    eq = equalize_gray_image_np(orig)

    # Lưu ảnh equalized (cùng tên ảnh gốc + hậu tố _equalized)
    out_path = image_path.rsplit('.',1)[0] + "_equalized.png"
    Image.fromarray(eq).save(out_path)
    print(f"✅ Đã lưu ảnh equalized: {out_path}")

    # 3️⃣ Phân tích ảnh equalized
    data_01 = eq.astype(np.float32) / 255.0
    plot_hist_pdf_cdf(
        data_01,
        title="Equalized: Histogram + PDF + CDF",
        xlabel="Mức xám chuẩn hóa (0–1)",
        threshold=threshold,
        bins=bins,
        save_path="Equalized_hist_pdf_cdf.png"
    )

    # 4️⃣ Hiển thị ảnh trước & sau để sinh viên so sánh
    fig, ax = plt.subplots(1,2, figsize=(9,4))
    ax[0].imshow(orig, cmap="gray", vmin=0, vmax=255)
    ax[0].set_title("Ảnh gốc")
    ax[0].axis("off")

    ax[1].imshow(eq, cmap="gray", vmin=0, vmax=255)
    ax[1].set_title("Ảnh sau Equalization")
    ax[1].axis("off")

    plt.suptitle("So sánh ảnh trước và sau Histogram Equalization")
    plt.tight_layout()
    plt.show()


# =====================================================
# MAIN: chạy thử
# =====================================================
if __name__ == "__main__":
    # 1️⃣ Ví dụ tổng hợp: Histogram + PDF + CDF + Threshold
    rng = np.random.default_rng(0)
    data = np.clip(rng.normal(loc=0.55, scale=0.12, size=4000), 0, 1)
    plot_hist_pdf_cdf(
        data,
        title="Ví dụ: Histogram + PDF + CDF (kiểu bài báo)",
        xlabel="Sd (chuẩn hóa [0,1])",
        threshold=0.78,
        bins=28,
        save_path="hist_pdf_cdf_example_style.png"
    )

    # 2️⃣ Task 2: chạy khi có ảnh thực tế
    # Uncomment dòng dưới khi có file image.jpg
    # analyze_before_after_equalization("image.jpg", threshold=0.5, bins=32)
