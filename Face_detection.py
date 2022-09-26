import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('img2.jpeg')	#choose an image to detect faces in

# convert img to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces, and return the coordinates of the rectangle
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)

# cv2.imshow('Face detected', grayscaled_img)	# show the image 
cv2.waitKey()	# waits untill any key is pressed


print("hell yeah... it's working!") # just to make sure my code works perfectly