import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img5.jpeg')	#choose an image to detect faces in

# convert img to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces, and return the coordinates of the face
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw rectangles around the faces
# (x, y, w, h) = face_coordinates[0]	==>  detects the 1st face only

# loop over the image and detect all faces
for (x, y, w, h) in face_coordinates:
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# print(face_coordinates)

cv2.imshow('Face detected', img)	# show the image 
cv2.waitKey()	# waits untill any key is pressed


print("hell yeah... it's working!") # just to make sure my code works perfectly