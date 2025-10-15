# 🤖 Real-Time Hand Gesture Classifier

A **low-latency computer vision application** that recognizes and classifies **hand gestures in real time** using a live webcam feed.  
This project demonstrates a complete **machine learning pipeline** — from **hand detection** and **image preprocessing** to **gesture classification** — built using **OpenCV**, **CVZone**, and a **TensorFlow/Keras** model.

---

## 🧠 Project Overview

The system detects a hand in the webcam feed, preprocesses the image dynamically, and classifies it into one of **36 gestures**, including:
- **Digits (0–9)**
- **ASL Alphabets (A–Z)**

It’s designed to be **lightweight**, **fast**, and **educational**, showing how real-time computer vision can integrate with deep learning for interactive applications.

---

## ✨ Key Features

- 🎥 **Real-Time Classification:**  
  Recognizes hand gestures with minimal latency and overlays the predicted label on the video feed.

- 🔤 **36 Gesture Support:**  
  Classifies both digits (0–9) and ASL alphabets (A–Z).

- ⚙️ **Dynamic Image Preprocessing:**  
  Automatically crops, scales, and normalizes detected hand images to a consistent **300×300 px** input for the CNN model.

- 🧩 **Visual Feedback:**  
  Displays live video feed, preprocessed image, and classification results side by side.

---

## 💻 Technologies Used

| Tool / Library | Purpose |
|-----------------|----------|
| **Python** | Primary programming language |
| **OpenCV (cv2)** | Video capture, drawing overlays, and visualization |
| **CVZone** | Simplified hand detection and gesture classification utilities |
| **TensorFlow / Keras** | Deep learning model framework |
| **NumPy** | Array operations and image manipulation |

---

## ⚙️ Installation and Setup

### 🧾 Prerequisites
- Python **3.x**
- A functional **webcam**

### 🏗️ Environment Setup
It’s recommended to use a **virtual environment**:

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install opencv-python numpy cvzone tensorflow
