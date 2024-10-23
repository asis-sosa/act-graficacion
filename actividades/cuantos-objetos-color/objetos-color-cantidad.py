# Cuantos objetos hay de cada color (Rojo, Amarillo, Verde, Azul, Celeste)
import cv2
import numpy as np

imagen = cv2.imread(r'D:\Sexto Semestre\Graficacion\cuantos-objetos-color\salida.png', 1)
imagen = cv2.resize(imagen, (0, 0), fx=0.5, fy=0.5)
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

bajo_rojo1 = np.array([0, 40, 40])
alto_rojo1 = np.array([10, 255, 255])
bajo_rojo2 = np.array([160, 40, 40])
alto_rojo2 = np.array([180, 255, 255])
amarillo_bajo = np.array([25, 40, 40])
amarillo_alto = np.array([35, 255, 255])
azul_bajo = np.array([90, 40, 40])
azul_alto = np.array([130, 255, 255])
celeste_bajo = np.array([80, 40, 40])
celeste_alto = np.array([100, 255, 255])
verde_bajo = np.array([35, 40, 40])
verde_alto = np.array([85, 255, 255])

mascara_rojo1 = cv2.inRange(imagen_hsv, bajo_rojo1, alto_rojo1)
mascara_rojo2 = cv2.inRange(imagen_hsv, bajo_rojo2, alto_rojo2)
mascara_rojo = cv2.add(mascara_rojo1, mascara_rojo2)
mascara_verde = cv2.inRange(imagen_hsv, verde_bajo, verde_alto)
mascara_amarillo = cv2.inRange(imagen_hsv, amarillo_bajo, amarillo_alto)
mascara_azul = cv2.inRange(imagen_hsv, azul_bajo, azul_alto)
mascara_celeste = cv2.inRange(imagen_hsv, celeste_bajo, celeste_alto)

def contar_objetos(mascara, umbral_pixeles):
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(mascara)
    objetos = 0
    for i in range(1, num_labels):
        if stats[i, cv2.CC_STAT_AREA] >= umbral_pixeles:
            objetos += 1
    return objetos

umbral_pixeles = 500

objetos_rojo = contar_objetos(mascara_rojo, umbral_pixeles)
objetos_verde = contar_objetos(mascara_verde, umbral_pixeles)
objetos_amarillo = contar_objetos(mascara_amarillo, umbral_pixeles)
objetos_azul = contar_objetos(mascara_azul, umbral_pixeles)
objetos_celeste = contar_objetos(mascara_celeste, umbral_pixeles)

print(f"Número de objetos con el color Rojo: {objetos_rojo}")
print(f"Número de objetos con el color Verde: {objetos_verde}")
print(f"Número de objetos con el color Amarillo: {objetos_amarillo}")
print(f"Número de objetos con el color Azul: {objetos_azul}")
print(f"Número de objetos con el color Celeste: {objetos_celeste}")

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
imagen_gris_bgr = cv2.cvtColor(imagen_gris, cv2.COLOR_GRAY2BGR)

resultado_rojo = np.where(mascara_rojo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_verde = np.where(mascara_verde[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_amarillo = np.where(mascara_amarillo[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_azul = np.where(mascara_azul[:, :, None] == 255, imagen, imagen_gris_bgr)
resultado_celeste = np.where(mascara_celeste[:, :, None] == 255, imagen, imagen_gris_bgr)

#cv2.imshow('Mascara Rojo', resultado_rojo)
#cv2.imshow('Mascara Verde', resultado_verde)
#cv2.imshow('Mascara Amarillo', resultado_amarillo)
#cv2.imshow('Mascara Azul', resultado_azul)
#cv2.imshow('Mascara Celeste', resultado_celeste)

#cv2.waitKey(0)
#cv2.destroyAllWindows()