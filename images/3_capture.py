import cv2 as cv
import time

cv.namedWindow('camera', cv.WINDOW_NORMAL)

capture = cv.VideoCapture(0)
result, img = capture.read()  #capture is a cv2.VideoCapture instance
ts = time.time()

i = 0
while True:
    result, img = capture.read()
    img = cv.resize(img, (800,600), 0, 0, cv.INTER_CUBIC);
    cv.imshow("camera", img)
    if cv.waitKey(10) == 32:
    	cv.imwrite(str(ts)+'_pic{:>05}.jpg'.format(i), img)
    	i += 1
    if cv.waitKey(10) == 27:
        break
    