import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
index = 1
while True:
    ret, frame = capture.read()
    if ret is True:
        cv.imshow("frame", frame)
        index += 1
        if index % 5 == 0:
            cv.imwrite("D:/day-01/" + str(index) + ".jpg", frame)
        c = cv.waitKey(50)
        if c == 27: # ESC
            break
    else:
        break

cv.destroyAllWindows()