import cv2
from random import randrange

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('img5.jpeg')	#==> hardcoded choosen image to detect faces in
# capture video from webcam
webcam = cv2.VideoCapture(0)

# iterate forever over frames

while True:

	# read the current frame
	successfulFrame_read, frame = webcam.read()
	
	# convert frame to grayscale
	grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces, and return the coordinates of the face
	face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

	# loop over the image and detect all faces
	for (x, y, w, h) in face_coordinates:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)	# ==> randrange() assigns a random value from 0 to 255

	cv2.imshow('Face detected', frame)	# Display the image with the faces
	cv2.waitKey(1)	# waits untill any key is pressed
"""
# Detect faces, and return the coordinates of the face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
# (x, y, w, h) = face_coordinates[0]	==>  detects the 1st face only

# loop over the image and detect all faces
for (x, y, w, h) in face_coordinates:
	cv2.rectangle(img, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)	# ==> randrange() assigns a random value from 0 to 255
# print(face_coordinates)

cv2.imshow('Face detected', img)	# Display the image with the faces
cv2.waitKey()	# waits untill any key is pressed

"""


print("hell yeah... it's working!") # just to make sure my code works perfectly

