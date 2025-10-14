import os
import shutil
import random

# Source and destination folders (edit these paths as needed)
source_folder_base = "data1"  # Base source folder (e.g., "data1")
destination_base_folder = "testdata"  # Base destination folder (e.g., "testdata")

# Define the labels (0-9 and A-Z)
labels = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]  # "0"-"9" and "A"-"Z"

# Loop through each label (0-9 and A-Z)
for label in labels:
    source_folder = os.path.join(source_folder_base, label)
    destination_folder = os.path.join(destination_base_folder, label)

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    # Get list of image files (you can customize extensions)
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    images = [f for f in os.listdir(source_folder) if f.lower().endswith(image_extensions)]

    # Check if there are enough images
    if len(images) < 20:
        print(f"Not enough images in the source folder: {source_folder}. Found only {len(images)} images.")
        selected_images = images  # Select all if fewer than 20 images
    else:
        # Select 20 random images
        selected_images = random.sample(images, 20)
        print(f"Selected 20 images from {source_folder}")

    # Copy the selected images to the destination folder
    for selected_image in selected_images:
        source_path = os.path.join(source_folder, selected_image)
        destination_path = os.path.join(destination_folder, selected_image)

        # Copy the selected image
        shutil.copy(source_path, destination_path)
        print(f"Copied '{selected_image}' to '{destination_folder}'")
