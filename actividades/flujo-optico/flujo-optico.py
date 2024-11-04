import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

ret, first_frame = cap.read()
prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)

ball_pos = np.array([[250, 250]], dtype=np.float32)
ball_pos = ball_pos[:, np.newaxis, :]

circulo_pos = ball_pos.copy()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    new_ball_pos, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos, None, **lk_params)

    if new_ball_pos is not None:
        ball_pos = new_ball_pos
        circulo_pos = new_ball_pos

    a, b = circulo_pos.ravel()
    frame = cv.circle(frame, (int(a), int(b)), 20, (0, 255, 0), -1)
    cv.rectangle(frame, (10, 10), (600, 500), (234, 43, 34), 5)  
    cv.imshow('Pelota en movimiento', frame)

    prev_gray = gray_frame.copy()

    if cv.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()