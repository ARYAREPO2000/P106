import cv2

frame = cv2.imread("walking.avi")

gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

faces = face_cascade.detectMultiScale(gray,1.1, 5)

print(len(faces))

for (x,y,w,h) in faces:
       
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)  

       # Crop the image to save the face image.
       roi_color = frame[y:y+h, x:x+w]
       cv2.imwrite("walking.avi",roi_color)
              
cv2.imshow('frame',frame)
cv2.waitKey(0)



