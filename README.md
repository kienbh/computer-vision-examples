# 🖼️ Computer Vision Examples: CSE3062-BCSE2022

This repository contains practical examples and lab exercises for the **Computer Vision** course (12 weeks, 4h/week).  
The goal is to help students build solid foundations in **Digital Image Processing (DIP)** and gain hands-on experience with  
**Deep Learning for Computer Vision**.  

Students will gradually learn how to:
1. Understand the principles of **digital imaging** (sampling, quantization, resolution).
2. Implement core **image processing algorithms** using OpenCV.
3. Explore **CNNs & YOLO** for object detection.
4. Experiment with **Vision-Language Models (VLMs)**.
5. Complete a **final project**: build and deploy a computer vision solution (API/App).

## 📂 Repository Structure
```
computer-vision-examples/
│
├── part1_DIP_weeks01-08/
│   ├── week01_digital_imaging_fundamentals/
│   │   └── digital_imaging_fundamentals.ipynb
│   ├── week02_point_processing/
│   │   ├── image_enhancement_point_processing.ipynb
│   │   ├── input/                  # sample images (Gonzalez & Woods)
│   │   ├── output/                 # generated results
│   │   └── output_bitplanes/       # bit-plane slicing results
│   ├── week03_histogram_processing/
│   │   ├── Image Enhancement Histogram Equalization.ipynb
│   │   ├── histogram_eq_present.py         # equalization demo (bar-chart comparison)
│   │   ├── histogram_match.py              # histogram matching (uniform/gaussian target)
│   │   ├── hist_pdf_cdf_visualization.py   # histogram + PDF + CDF plots
│   │   ├── equalized_histogram_stem_plot.py
│   │   └── input/                  # sample images
│   ├── week04_spatial_filtering/
│   │   └── Image Enhancement Spatial Filtering.ipynb
│   ├── week05_frequency_domain/
│   │   ├── Frequency Domain Processing.ipynb
│   │   └── input/                  # images used by the examples & exercises
│   ├── week06_pca_lossless_compression/
│   │   ├── PCA and Lossless Compression.ipynb
│   │   └── input/
│   ├── week07_restoration_morphology/
│   │   ├── Restoration and Morphological Processing.ipynb
│   │   └── input/
│   └── week08_segmentation_jpeg/
│       ├── Segmentation and JPEG.ipynb
│       └── input/
│
├── part2_DL_CV_weeks09-10/
│   ├── week09_cnn_yolo/                    # (coming soon)
│   └── week10_multimodal_cv/               # (coming soon)
│
├── Gonzalez_images/          # sample images from Gonzalez & Woods, DIP 3rd ed. (CH01–CH12)
├── requirements.txt
└── README.md
```

## 🖼️ Sample Images
The folder `Gonzalez_images/` contains the original sample images from the textbook
**R. C. Gonzalez & R. E. Woods, *Digital Image Processing*, 3rd edition** (chapters 1–12),
used by the weekly notebooks. These images are provided **for educational use only**
as companion material of the textbook.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/kienbh/computer-vision-examples.git
cd computer-vision-examples
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate          # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 📚 Course Topics Covered
```
Introduction on Digital Image Processing and Computer Vision

  Phần 1: Digital Image Processing - DIP (Weeks 1–8)
    - Digital Imaging Fundamentals
    - Image Enhancement (Point Processing)
    - Histogram Processing
    - Spatial Filtering
    - Frequency Domain Processing
    - PCA & Image Compression (Lossless)
    - Image Restoration & Morphological Processing
    - Image Segmentation & JPEG Standard
  
  Phần 2: Deep Learning for CV (Weeks 9–10)
    - CNNs & YOLOs for Object Detection
    - Multi-modal LLMs & Applications in CV
  
  Phần 3: Final Project (Weeks 11–12)
    - Data Collection, Labeling & Model Training
    - Deployment & Presentation (API deployment / App demo)
```

## 📝 Assignments & Evaluation
- **Midterm Assignment (30%)**: Implement DIP algorithms (OpenCV).  
- **Final Project (50%)**: Build a CV solution (data collection, training, API/App demo).  
- **Class Participation (10%)**: Attendance
- **Final Presentation (10%)**: activities, presentations, teamwork.
  
## 👨‍🏫 Instructor
**Dr. Bùi Huy Kiên**
Lecturer, Vietnam Japan University (VJU)  
Course:CSE3062 Computer Vision – Bachelor of Computer Science & Engineering (BCSE2022)  

## 📌 Notes
- This repo is for **educational purposes only**.  
- Students are encouraged to **fork** and submit their assignments/projects via GitHub.  
- Contributions (pull requests) are welcome for improving examples.  

