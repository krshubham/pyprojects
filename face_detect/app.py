# #All the software dependencies
# try:
# 	import numpy as np
# 	import cv2
# except ImportError:
# 	print("Error in importing the dependencies")


# # img = cv2.imread('obama.jpg',0)
# # #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
# # #The function waits for specified milliseconds for any keyboard event
# # cv2.imshow('image',img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()


# #Code for some more video playing stuff
# # cap = cv2.VideoCapture(0)
# # while(True):
# #     # Capture frame-by-frame
# #     ret, frame = cap.read()

# #     # Our operations on the frame come here
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# #     # Display the resulting frame
# #     cv2.imshow('frame',gray)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #     	break

# # # When everything done, release the capture
# # cap.release()
# # cv2.destroyAllWindows()

# #//////////////////////////////////
# #COde for mouse as a brush

# # def draw_circle(event,x,y,flags,param):
# #     if event == cv2.EVENT_LBUTTONDBLCLK:
# #         cv2.circle(img,(x,y),100,(255,0,0),-1)

# # # Create a black image, a window and bind the function to window
# # img = np.zeros((512,512,3), np.uint8)
# # cv2.namedWindow('image')
# # cv2.setMouseCallback('image',draw_circle)

# # while(1):
# #     cv2.imshow('image',img)
# #     if cv2.waitKey(0) & 0xFF == 27:
# #         break
# # cv2.destroyAllWindows()


# #/////////////////////////////
# #COde for object detection

# # import cv2
# # import numpy as np

# # cap = cv2.VideoCapture(0)

# # while(1):

# #     # Take each frame
# #     _, frame = cap.read()

# #     # Convert BGR to HSV
# #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# #     # define range of blue color in HSV
# #     lower_blue = np.array([110,50,50])
# #     upper_blue = np.array([130,255,255])

# #     # Threshold the HSV image to get only blue colors
# #     mask = cv2.inRange(hsv, lower_blue, upper_blue)

# #     # Bitwise-AND mask and original image
# #     res = cv2.bitwise_and(frame,frame, mask= mask)

# #     cv2.imshow('frame',frame)
# #     cv2.imshow('mask',mask)
# #     cv2.imshow('res',res)
# #     k = cv2.waitKey(5) & 0xFF
# #     if k == 27:
# #         break

# # cv2.destroyAllWindows()

# #/////////////////////////////
# #Code for edge tracking
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('messi5.jpg',0)
# edges = cv2.Canny(img,100,200)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('obama.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()