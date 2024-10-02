import numpy as np
import cv2

def generar_punto_elipse_mercury(a, b, t):
    x = int(a * np.cos(t) + 550)
    y = int(b * np.sin(t) + 375)
    return (x, y)

img_width, img_height = 1100, 750
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

mercuryX = 200
mercuryY = 100

venusX = 220
venusY = 120

earthX = 240
earthY = 140

marsX = 270
marsY = 170

jupiterX = 320
jupiterY = 210

saturnX = 380
saturnY = 270

uranusX = 430
uranusY = 310

neptuneX = 470
neptuneY = 350

num_puntos_mercury = 500

t_vals = np.linspace(0, 2 * np.pi, num_puntos_mercury)
for t in t_vals:
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    # Circulo Principal (Sol)
    cv2.circle(imagen, (550, 375), 45, (40, 176, 255), 90)

    # Elipse de Mercurio
    punto_mercury = generar_punto_elipse_mercury(mercuryX, mercuryY, t)
    cv2.circle(imagen, punto_mercury, radius=5, color=(169, 169, 169), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(mercuryX, mercuryY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Venus
    punto_venus = generar_punto_elipse_mercury(venusX, venusY, t)
    cv2.circle(imagen, punto_venus, radius=6, color=(140, 180, 210), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(venusX, venusY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de la Tierra
    punto_earth = generar_punto_elipse_mercury(earthX, earthY, t)
    cv2.circle(imagen, punto_earth, radius=6, color=(148, 105, 0), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(earthX, earthY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Marte
    punto_mars = generar_punto_elipse_mercury(marsX, marsY, t)
    cv2.circle(imagen, punto_mars, radius=5, color=(50, 39, 188), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(marsX, marsY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Jupiter
    punto_jupiter = generar_punto_elipse_mercury(jupiterX, jupiterY, t)
    cv2.circle(imagen, punto_jupiter, radius=25, color=(63, 133, 205), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(jupiterX, jupiterY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Saturno
    punto_saturn = generar_punto_elipse_mercury(saturnX, saturnY, t)
    cv2.circle(imagen, punto_saturn, radius=20, color=(32, 165, 218), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(saturnX, saturnY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Urano
    punto_uranus = generar_punto_elipse_mercury(uranusX, uranusY, t)
    cv2.circle(imagen, punto_uranus, radius=15, color=(230, 216, 173), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(uranusX, uranusY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    # Elipse de Neptuno
    punto_neptune = generar_punto_elipse_mercury(neptuneX, neptuneY, t)
    cv2.circle(imagen, punto_neptune, radius=15, color=(255, 0, 0), thickness=-1)
    for t_tray in t_vals:
        pt_tray = generar_punto_elipse_mercury(neptuneX, neptuneY, t_tray)
        cv2.circle(imagen, pt_tray, radius=1, color=(255, 255, 255), thickness=-1)

    cv2.imshow('img', imagen)
    cv2.waitKey(10)

cv2.destroyAllWindows()