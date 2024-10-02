# Actividada 1
import cv2 as cv
import numpy as np
import math

# Se agrega la imagen
img = cv.imread(r"D:\Sexto Semestre\Graficacion\pixel_art_cer0.jpg", 0)

# Se obtiene las dimensiones de la imagen
x, y = img.shape[0], img.shape[1]

# Rotacion de la imagen a 60 grados en sentido contrario al reloj
angle = 60
theta = math.radians(angle)
rotation_matrix = cv.getRotationMatrix2D((y // 2, x // 2), angle, 1)
rotated_img = cv.warpAffine(img, rotation_matrix, (x, y))

# Traslacion de la imagen en 10
tx, ty = 10, 10
translation_matrix = np.float32(([1, 0, tx], [0, 1, ty]))
translated_img = cv.warpAffine(rotated_img, translation_matrix, (x, y))

# Escalamiento de la imagen en una quinta parte (1/5)
scale_factor = 1/5
scaled_img = cv.resize(translated_img, None, fx = scale_factor, fy = scale_factor)

# Actividad 2

# Se hace rotar la imagen 30 grados en sentido al reloj
angle_right = 30
rotation_matrix_right = cv.getRotationMatrix2D((y // 2, x // 2), angle_right, 2)
rotated_right_img = cv.warpAffine(img, rotation_matrix_right, (y * 2, x * 2))

# Se hace rotar la imagen 60 grados hacia sentido contrario al reloj
angle_left = -60
rotation_matrix_left = cv.getRotationMatrix2D((y // 2, x // 2), angle_left, 2)
rotated_left_img = cv.warpAffine(img, rotation_matrix_left, (y * 2, x * 2))

# Actividad 3

# Se hace rotar la imagen 70 grados en sentido contrario al reloj, junto con un escalamiento en 2
angleA3 = 70
scale_factor_A3 = 2
rotation_matrix_A3 = cv.getRotationMatrix2D((y // 2, x // 2), angleA3, scale_factor_A3)
rotated_img_A3 = cv.warpAffine(img, rotation_matrix_A3, (y * scale_factor_A3, x * scale_factor_A3))

# Se traslada la imagen 20 pixeles
tx, ty = 20, 20
translation_matrix_A3 = np.float32([[1, 0, tx], [0, 1, ty]])
translated_img = cv.warpAffine(rotated_img_A3, translation_matrix_A3, (int(y * scale_factor_A3), int(x * scale_factor_A3)))

# Muestra de los cambios efectuados a la imagen
cv.imshow('Imagen original', img)
cv.imshow('Imagen con los cambios efectuados Actividad 1', scaled_img)
cv.imshow('Imagen con los cambios efectuados Actividad 2', rotated_right_img)
cv.imshow('Imagen con los cambios efectuados Actividad 2', rotated_left_img)
cv.imshow('Imagen con los cambios efectuados Actividad 3', translated_img)
cv.waitKey(0)
cv.destroyAllWindows()