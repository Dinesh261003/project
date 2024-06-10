import cv2 
from datetime import datetime
import sys
import capture

# Load trained recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('C:/Users/91900/home_security/trainer/trainer.yml')

# Load face cascade classifier
cascadePath = "C:/Users/91900/home_security/Opencv-Face/FacialRecognition/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# Font for displaying text on images
font = cv2.FONT_HERSHEY_SIMPLEX

# Names related to ids
names = ['None', 'dharshana'] 

# Initialize video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

# Define parameters for unknown face detection
unknown_confidence_threshold = 50  # Adjust this threshold according to your needs
unknown_detection_delay = 5  # Number of frames to wait before considering a face as unknown
capture_delay = 5  # Number of seconds to wait before capturing the camera

unknown_start_time = None
is_unknown_detected = False

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Recognize the face
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Check if confidence is less than a certain threshold
        if confidence < 100:
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            is_unknown_detected = False  # Reset unknown detection flag
            unknown_start_time = None  # Reset unknown detection timer
        else:
            if unknown_start_time is None:
                unknown_start_time = datetime.now()  # Start the timer if an unknown face is detected
            else:
                elapsed_time = (datetime.now() - unknown_start_time).total_seconds()
                if elapsed_time >= unknown_detection_delay:
                    # If more than the delay has passed, consider the face as unknown
                    id = 1  # Label unknown faces as 1
                    confidence = "  {0}%".format(round(100 - confidence))
                    is_unknown_detected = True

                    if elapsed_time >= capture_delay:
                        # Capture and save the camera image
                        capture_image = img.copy()
                        cv2.imwrite('unknown_person.jpg', capture_image)
                        print("Camera captured due to unknown face detected")
                        image_path='C:/Users/91900/Desktop/home_security/Opencv-Face/FacialRecognition/unknown_person.jpg'
                        cam.release()
                        cv2.destroyAllWindows()
                        capture.captureall(image_path)
                    
                        sys.exit()
                        # You can add additional actions here, such as sending an alert or triggering an alarm

        # Display the recognized name and confidence level
        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        

    # Display the camera feed
    cv2.imshow('camera', img)

    # Check for ESC key press to exit the program
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
