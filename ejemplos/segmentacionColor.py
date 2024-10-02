import cv2 as cv

img = cv.imread('fl4k_prueba.jpeg', 1)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

uba = (15, 255, 255)
ubb = (90, 60, 90)

uba2 = (180, 255, 255)
ubb2 = (170, 40, 40)

mask1 = cv.inRange(hsv, ubb, uba)
mask2 = cv.inRange(hsv, ubb2, uba2)

mask = mask1 + mask2


res = cv.bitwise_and(img, img, mask=mask)

cv.imshow('res', res)
cv.imshow('hsv', hsv)
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()