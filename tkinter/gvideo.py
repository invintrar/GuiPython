import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

# Get the Default resolutions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

codec = cv2.VideoWriter_fourcc('M','J','P','G')

name = 'video-' + time.strftime('%d-%m-%Y-%X')+'.avi'
print(name)
# Define the codec and filename.
out = cv2.VideoWriter('output1.avi', codec, 10, (frame_width,frame_height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the  frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()