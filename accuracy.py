import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
import numpy as np
import os


model = load_model("Model/keras_model.h5")


labels = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]
print("Labels:", labels)
print("Model output shape:", model.output_shape)


test_dir = "testdata"
correct = 0
total = 0
accuracy_per_class = []

for label in labels:
    class_dir = os.path.join(test_dir, label)
    class_correct = 0
    class_total = 0

    if not os.path.exists(class_dir):
        print(f"Missing folder: {class_dir}, skipping...")
        accuracy_per_class.append(0)
        continue

    for img_name in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        img = cv2.resize(img, (224, 224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img, verbose=0)
        predicted_index = np.argmax(prediction)

        if predicted_index >= len(labels):
            print(f"Warning: Prediction index {predicted_index} out of range.")
            continue

        predicted_label = labels[predicted_index]

        if predicted_label == label:
            class_correct += 1
        class_total += 1

    if class_total == 0:
        accuracy_per_class.append(0)
        continue

    accuracy = (class_correct / class_total) * 100
    accuracy_per_class.append(accuracy)
    total += class_total
    correct += class_correct


plt.figure(figsize=(18, 5))
plt.bar(labels, accuracy_per_class, color='skyblue')
plt.xlabel("Sign")
plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy per Sign")
plt.ylim([0, 100])
plt.show()

if total > 0:
    print(f"Overall Accuracy: {correct/total * 100:.2f}%")
else:
    print("No images found.")
