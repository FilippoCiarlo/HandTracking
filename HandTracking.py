import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0   # previous time
cTime = 0   # current time

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)

                # h = heigth, w = width, c = channel
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

                if id == 4:
                    cv2.circle(img, (cx,cy), 15, (80, 255, 222), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # calculate FPS
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # visualize output
    cv2.putText(img, f"FPS:{str(int(fps))}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (80, 255, 222), 2)
    cv2.imshow("HandTracking", img)
    cv2.waitKey(1)