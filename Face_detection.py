import cv2

# load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_dat = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces in
img = cv2.imread('img1.jpeg')

# show the image 
cv2.imshow('Face detected', img)

# waits untill any key is pressed
cv2.waitKey()


print("hell yeah... it's working!")