# Amarillo, Verde, Azul, Magenta y Rojo
import cv2
import numpy as np

# Leer la imagen en formato RGB
imagen = cv2.imread(r'D:\Sexto Semestre\Graficacion\efecto-gris-npwhere\arcoiris-prueba.jpg', 1)

# Redimensionar la imagen a un tamaño más pequeño (por ejemplo, al 50% del tamaño original)
imagen = cv2.resize(imagen, (0, 0), fx=0.5, fy=0.5)

# Convertir la imagen de RGB a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Definir el rango de color rojo en HSV
bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])
amarillo_bajo = np.array([25, 40, 40])
amarillo_alto = np.array([35, 255, 255])
azul_bajo = np.array([90, 40, 40])
azul_alto = np.array([130, 255, 255])
magenta_bajo = np.array([140, 40, 40])
magenta_alto = np.array([170, 255, 255])

# Definir el rango de color verde en HSV
verde_bajo = np.array([35, 40, 40])  # Ajuste para el verde
verde_alto = np.array([85, 255, 255])

# Crear máscaras para los colores
mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_verde = cv2.inRange(imagen_hsv, verde_bajo, verde_alto)
mascara_amarillo = cv2.inRange(imagen_hsv, amarillo_bajo, amarillo_alto)
mascara_azul = cv2.inRange(imagen_hsv, azul_bajo, azul_alto)
mascara_magenta = cv2.inRange(imagen_hsv, magenta_bajo, magenta_alto)

# Sumar la mascara de rojo
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)

# Convertir la imagen original a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir la imagen gris a un formato BGR para que coincida con la original
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

# Combinar la imagen en gris con las áreas en rojo y verde
resultado_rojo = np.where(mascara_rojo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_verde = np.where(mascara_verde[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_amarillo = np.where(mascara_amarillo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_azul = np.where(mascara_azul[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_magenta = np.where(mascara_magenta[:, :, None] == 255, imagen, imagen_gris_bgr)

# Mostrar cada máscara de color en una ventana separada
cv2.imshow('Mascara Rojo', resultado_rojo)
cv2.imshow('Mascara Verde', resultado_verde)
cv2.imshow('Mascara Amarillo', resultado_amarillo)
cv2.imshow('Mascara Azul', resultado_azul)
cv2.imshow('Mascara Magenta', resultado_magenta)

# Esperar a que se presione una tecla y cerrar todas las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()