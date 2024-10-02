import cv2 as cv
import numpy as np

img = np.ones((500, 500), dtype = np.uint8) * 255
# Los primeros numeros (500, 500) son el alto y anchor de la imagen,
# respectivamente (Se involucran los 255 tonos de colores)

cv.circle(img, (250, 250), 4, (0, 0, 0), 2)
# Los primeros numeros (250, 250) son la posicion del circulo en la imagen

img2 = np.ones((500, 500, 3), dtype = np.uint8) * 255
# El numero 3 significa la cantidad de canales de color que se usaran

cv.circle(img2, (250, 250), 50, (0, 234, 21), -1)
# El segundo numero (50) representa el tamaño en pixeles del circulo

cv.line(img2, (1, 1), (230, 240), (0, 234, 21), 3)
# Los terceros numeros (0, 234, 21) representan los colores RGB del circulo
# Los colores estan formados por B - G - R

img3 = np.ones((500, 500, 3), dtype = np.uint8) * 255
cv.circle(img3, (250, 250), 50, (0, 234, 21), -1)
cv.line(img3, (1, 1), (230, 240), (0, 234, 21), 3)
cv.rectangle(img3, (20, 20), (50, 60), (0, 0, 0), 3)
# Los valores (20, 20) representan la posicion en (x, y) del vertice o punta superior izquierdo
# Los valores (50, 60) representan la posicion en (x, y) del vertice o punta inferior derecho
# El ultimo valor (3) es el grosor que tiene la figura.

img4 = np.ones((500, 500, 3), dtype = np.uint8) * 255
cv.circle(img4, (250, 250), 50, (0, 234, 21), -1)
cv.circle(img4, (250, 250), 30, (0, 0, 0), -1)
cv.line(img4, (1, 1), (230, 240), (0, 234, 21), 3)
cv.rectangle(img4, (20, 20), (50, 60), (0, 0, 0), 3)


img5 = np.ones((500, 500, 3), dtype = np.uint8) * 255
cv.circle(img5, (250, 250), 50, (0, 234, 21), -1)
cv.circle(img5, (250, 250), 30, (0, 0, 0), -1)
cv.line(img5, (1, 1), (230, 240), (0, 234, 21), 3)
cv.rectangle(img5, (20, 20), (50, 60), (0, 0, 0), 3)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img5, [pts], True, (0, 0, 0), 3)

# Crear una imagen en blanco
img6 = np.ones((500, 500, 3), dtype = np.uint8) * 255

# Definir los vértices del triángulo
pts = np.array([[20, 20], [50, 60], [80, 20]], np.int32)
pts = pts.reshape((-1, 1, 2))
pts2 = np.array([[100, 100], [200, 300], [300, 100]], np.int32)
pts2 = pts2.reshape((-1, 1, 2))

# Dibujar el triángulo
cv.polylines(img6, [pts], isClosed=True, color=(0, 0, 0), thickness=3)
cv.polylines(img6, [pts2], isClosed=True, color=(0, 0, 0), thickness=3)

# Mostrar la imagen
# cv.imshow('Imagen', img)
# cv.imshow('Imagen2', img2)
# cv.imshow('Imagen3', img3)
# cv.imshow('Imagen4', img4)
# cv.imshow('Imagen5', img5)
cv.imshow('Triangulo', img6)
cv.waitKey()
cv.destroyAllWindows()