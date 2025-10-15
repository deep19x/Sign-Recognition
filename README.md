Real-Time Hand Gesture Classifier
Project Overview
This project implements a low-latency computer vision application capable of recognizing and classifying hand gestures in real-time from a live webcam feed. Built primarily with OpenCV and the CVZone framework, it utilizes a pre-trained Keras/TensorFlow model to classify the hand signs, which include numbers (0−9) and the American Sign Language (ASL) alphabet (A−Z).

The primary goal is to demonstrate a functional machine learning pipeline that handles real-time object detection (hand localization) followed by image preprocessing and classification.

✨ Key Features
Real-Time Classification: Performs continuous gesture recognition with low latency, displaying the predicted label directly onto the live video stream.

36 Gesture Support: Capable of classifying 36 distinct hand signs (10 digits and 26 letters).

Dynamic Image Preprocessing: Automatically detects the hand using bounding box coordinates and applies dynamic scaling and padding to normalize the captured image into a consistent 300×300 pixel input for the CNN model.

Visual Feedback: Provides simultaneous visualization of the raw camera feed, the cropped and normalized image (for model input verification), and a reference image.

💻 Technologies Used
Tool/Library

Purpose

Python

Primary development language.

OpenCV (cv2)

Core computer vision tasks, including video capture, image display, and drawing overlays.

CVZone

Simplified hand detection and ML classification utilities.

Keras / TensorFlow

Framework used for the underlying classification model (keras_model.h5).

NumPy

Array manipulation for image processing tasks.

⚙️ Installation and Setup
Prerequisites
Python 3.x (Recommended)

A functional webcam.

Environment Setup
It is highly recommended to use a virtual environment (venv).

# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 2. Install required libraries
pip install opencv-python numpy cvzone tensorflow

Model Files (Crucial Step)
The project relies on two files that are required for classification. Since large files are typically not pushed to GitHub, you need to ensure they are available locally:

Model/keras_model.h5: The trained CNN model file.

Model/labels.txt: A text file listing the 36 labels in the correct order.

Ensure you place these files in a folder named Model/ in the root of your project directory.

▶️ How to Run the Application
Ensure your virtual environment is active.

Run the main Python script (assuming the file is named main.py):

python main.py

A window will open displaying your live webcam feed with the predicted gesture label overlaid.
