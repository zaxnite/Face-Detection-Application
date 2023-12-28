import cv2
import numpy as np 

face_classifier = cv2.CascadeClassifier('face_detection_venv\haarcascade_frontalface_default.xml')

def detect_faces(img): #Performing face detection using images inputed 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting input img to grayscale
    faces = face_classifier.detectMultiScale(gray,1.3,5) 
    if faces is ():
        return img

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    return img

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = detect_faces(frame)

    cv2.imshow('Video Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit program
        break

cap.release()
cv2.destroyAllWindows()