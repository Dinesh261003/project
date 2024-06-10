import cv2
import os

# Create a directory to store the dataset if it doesn't exist
dataset_dir = 'dataset'
if not os.path.exists(dataset_dir):
    os.makedirs(dataset_dir)

# Initialize the video capture device
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

# Load the face detector
face_detector = cv2.CascadeClassifier('C:/Users/91900/home_security/Opencv-Face/FacialRecognition/haarcascade_frontalface_default.xml')

while True:
    # Prompt for the user ID
    user_id = input('\nEnter user ID and press <Enter>: ')
    try:
        user_id = int(user_id)
        break  # Exit the loop if the user ID is valid
    except ValueError:
        print("Invalid input. Please enter a numeric user ID.")

print("\n [INFO] Initializing face capture. Look at the camera and wait...")

# Initialize the sample count
sample_count = 0

# Capture 50 samples
while True:
    # Read a frame from the video capture device
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip video image horizontally for selfie view
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Process each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        sample_count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite(f"{dataset_dir}/User.{user_id}.{sample_count}.jpg", gray[y:y+h, x:x+w])
        print(f"Image saved: User {user_id}, Sample {sample_count}")

    # Display the captured frame with rectangles around faces
    cv2.imshow('Captured Face', img)

    # Check for ESC key press to exit the loop or if 100 samples are captured
    k = cv2.waitKey(100) & 0xff
    if k == 27 or sample_count >= 100:
        break

# Cleanup
print("\n[INFO] Exiting program and cleaning up...")
cam.release()
cv2.destroyAllWindows()
