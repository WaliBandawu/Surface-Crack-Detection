# Surface-Crack-Detection

## Overview
This project is a **Surface Crack Detection Web Application** built using Flask. It leverages a pre-trained deep learning model (`dima806/surface_crack_image_detection`) from the Hugging Face Transformers library for image classification. Users can upload images to detect surface cracks, and the app provides predictions with annotated images.

---

## Features
- **Image Classification**: Classifies images to detect surface cracks with confidence scores.
- **Image Annotation**: Annotates uploaded images with the top prediction label and confidence.
- **Web Interface**: Intuitive HTML-based user interface for uploading images and viewing results.
- **Static Image Storage**: Uploaded and annotated images are stored in dedicated folders.

---

## Prerequisites
- **Python**: Install Python 3.8 or higher.
- **Libraries**:
  - Flask
  - Transformers
  - Pillow
- **Folder Setup**:
  - `static/uploads`: To store uploaded images.
  - `static/annotated`: To store annotated images.

---
