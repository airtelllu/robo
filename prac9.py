##import cv2
###reading the image
##img = cv2.imread("C://User//Durga//OneDrive//Desktop//face.jpg")
###converting image to grayscale
##gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
###Loading the required haar-cascade.xml classifier file
##haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
##eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
##faces_rect = haar_cascade.detectMultiScale(gray_img, 1.3, 5)
##eyes = eye_cascade.detectMultiScale(gray_img)
##for(x, y, w ,h) in faces_rect:
##    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
##    for(ex, ey, ew ,eh) in eyes:
##        cv2.rectangle(img, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
##cv2.imshow('Detected faces', img)
##cv2.waitKey(0)


import cv2

# Reading the image
img = cv2.imread("C:\\Users\\Durga\\OneDrive\\Desktop\\face.jpg")

# Converting image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Loading the required haar-cascade.xml classifier file
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Detecting faces and eyes
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.3, 5)
eyes = eye_cascade.detectMultiScale(gray_img)

# Drawing rectangles around detected faces and eyes
for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# Displaying the image with detected faces and eyes
cv2.imshow('Detected faces and eyes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
