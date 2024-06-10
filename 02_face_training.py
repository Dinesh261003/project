import cv2
import numpy as np
import os

# Path for face image database
dataset_path = 'dataset'
trainer_path = 'C:/Users/91900/home_security/trainer'

# LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Function to preprocess images
def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization
    gray = cv2.equalizeHist(gray)
    return gray

# Function to get the images and labels for training
def get_images_and_labels(dataset_path):
    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        # Read the image
        image = cv2.imread(image_path)
        # Preprocess the image
        processed_image = preprocess_image(image)
        # Extract the label (id) from the filename
        label = int(os.path.splitext(os.path.basename(image_path))[0].split(".")[1])
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(processed_image, scaleFactor=1.2, minNeighbors=5)
        for (x, y, w, h) in faces:
            # Extract the face region
            face_roi = processed_image[y:y+h, x:x+w]
            # Resize the face region to a fixed size (e.g., 100x100)
            face_roi = cv2.resize(face_roi, (100, 100))
            # Add the face sample and label to the lists
            face_samples.append(face_roi)
            ids.append(label)

    return face_samples, ids

# Load the pre-trained face cascade classifier
face_cascade = cv2.CascadeClassifier("C:/Users/91900/home_security/Opencv-Face/FacialRecognition/haarcascade_frontalface_default.xml")

# Get the face samples and corresponding labels
face_samples, ids = get_images_and_labels(dataset_path)

# Train the recognizer
recognizer.train(face_samples, np.array(ids))

# Save the trained model
recognizer.save(os.path.join(trainer_path, 'trainer.yml'))

print("Training completed successfully.")
