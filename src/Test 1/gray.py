import numpy as np
import cv2

#importing the All the face-detecting Cascade
face_detector1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_detector2 = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
face_detector3 = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
face_detector4 = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

#Reading the file
img = cv2.imread('index.jpeg')
#Converting it to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detect face using 4 different classifiers
faces1 = face_detector1.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
faces2 = face_detector2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
faces3 = face_detector3.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
faces4 = face_detector4.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)

#Crop the gray image to only face
for (x,y,w,h) in faces1:
	gray = gray[y:y+h, x:x+w]

#Resize the image and output.
try:
    out = cv2.resize(gray, (350, 350)) #Resize face so all images have same size
    cv2.imwrite("index1.jpeg", out) #Write image
except:
    pass

#Crop the gray image to only face
for (x,y,w,h) in faces2:
    gray = gray[y:y+h, x:x+w]

#Resize the image and output.
try:
    out = cv2.resize(gray, (350, 350)) #Resize face so all images have same size
    cv2.imwrite("index2.jpeg", out) #Write image
except:
    pass

#Crop the gray image to only face
for (x,y,w,h) in faces3:
    gray = gray[y:y+h, x:x+w]

#Resize the image and output.
try:
    out = cv2.resize(gray, (350, 350)) #Resize face so all images have same size
    cv2.imwrite("index3.jpeg", out) #Write image
except:
    pass

#Crop the gray image to only face
for (x,y,w,h) in faces4:
    gray = gray[y:y+h, x:x+w]

#Resize the image and output.
try:
    out = cv2.resize(gray, (350, 350)) #Resize face so all images have same size
    cv2.imwrite("index4.jpeg", out) #Write image
except:
    pass