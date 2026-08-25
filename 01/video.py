import cv2 as cv
import time

cap = cv.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("can't open camera by index")

isGrayScale = False

while True:
    _ret , frame = cap.read()

    if(not _ret):
        raise RuntimeError("can't read img")

    if isGrayScale:
        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    cv.imshow("camera", frame)

    key = cv.waitKey(1) & 0xFF

    if( key == ord('q') ):
        break

    if( key == ord('c') ):
        isGrayScale = not isGrayScale
    
    if( key == ord('s') ):
        cv.imwrite(f"{int(time.time())}ali.png",frame)

cap.release()
cv.destroyAllWindows()