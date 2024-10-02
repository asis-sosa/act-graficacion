import cv2 as cv
import numpy as np

img = np.ones((600, 800, 3), dtype = np.uint8) * 255

# Circulo Principal
cv.circle(img, (400, 300), 130, (137, 21, 17), 300)

# Circulos que figuran una luna a la mitad
cv.circle(img, (530, 120), 40, (255, 255, 255), 100)
cv.circle(img, (480, 170), 40, (137, 21, 17), 100)

# Circulos que representan una montaña en forma de corazon
cv.circle(img, (400, 425), 70, (105, 15, 12), 170)
cv.circle(img, (345, 410), 70, (105, 15, 12), 170)
cv.circle(img, (300, 370), 70, (105, 15, 12), 170)
cv.circle(img, (470, 405), 70, (105, 15, 12), 170)
cv.circle(img, (500, 370), 70, (105, 15, 12), 170)

# Circulos que figuran estrellas
cv.circle(img, (300, 150), 2, (255, 255, 255), 10)
cv.circle(img, (250, 110), 3, (255, 255, 255), 10)
cv.circle(img, (220, 140), 1, (255, 255, 255), 10)
cv.circle(img, (340, 140), 2, (255, 255, 255), 10)
cv.circle(img, (380, 150), 3, (255, 255, 255), 10)
cv.circle(img, (440, 120), 1, (255, 255, 255), 10)
cv.circle(img, (380, 90), 2, (255, 255, 255), 10)
cv.circle(img, (450, 170), 3, (255, 255, 255), 10)
cv.circle(img, (490, 150), 1, (255, 255, 255), 10)
cv.circle(img, (200, 180), 2, (255, 255, 255), 10)
cv.circle(img, (300, 120), 3, (255, 255, 255), 10)
cv.circle(img, (250, 160), 1, (255, 255, 255), 10)
cv.circle(img, (170, 210), 2, (255, 255, 255), 10)
cv.circle(img, (340, 180), 3, (255, 255, 255), 10)
cv.circle(img, (340, 70), 1, (255, 255, 255), 10)
cv.circle(img, (410, 200), 2, (255, 255, 255), 10)
cv.circle(img, (510, 120), 3, (255, 255, 255), 10)
cv.circle(img, (530, 170), 1, (255, 255, 255), 10)
cv.circle(img, (410, 60), 2, (255, 255, 255), 10)
cv.circle(img, (620, 200), 3, (255, 255, 255), 10)

# Arbol de la montaña (Tronco)
cv.rectangle(img, (300, 400), (300, 200), (70, 7, 5), 80)

# Arbol de la montaña (Hojas)
cv.circle(img, (250, 220), 40, (47, 3, 2), 90)
cv.circle(img, (350, 220), 40, (47, 3, 2), 90)
cv.circle(img, (300, 150), 40, (47, 3, 2), 90)

# Arbol de la montaña (Manzana)
cv.circle(img, (380, 310), 2, (47, 3, 2), 10)

cv.imshow('Imagen', img)
cv.waitKey()
cv.destroyAllWindows()