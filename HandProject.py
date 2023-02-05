import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime = 0  # previous time
cTime = 0  # current time
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        # Thumb, Index, Middle, Ring, Pinky
        print("T",lmList[4],": I",lmList[8],": M",lmList[12],": R",lmList[16],": P",lmList[20])

    # calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # visualize output
    cv2.putText(img, f"FPS:{str(int(fps))}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (80, 255, 222), 2)
    cv2.imshow("HandTracking", img)
    cv2.waitKey(1)