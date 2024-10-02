import numpy as np
import cv2


width, height = 900, 750 
img = np.ones((height, width, 3), dtype=np.uint8)*255

a, b = 150, 100
k = 10
theta_increment = 0.05
max_theta = 2 * np.pi

center_x, center_y = width // 2, height // 2

theta = 0

while True:
    img = np.ones((height, width, 3), dtype=np.uint8) * 255
    
    for t in np.arange(0, theta, theta_increment):
        r = a + b * np.cos(k * t)

        # Ecuacion parametrica para el circulo
        circuloX = int(center_x + a * np.cos(t))
        circuloY = int(center_y + a * np.sin(t))

        cv2.circle(img, (circuloX, circuloY), 1, (102, 0, 0), 1)
        cv2.circle(img, (circuloX-2, circuloY-2), 1, (0, 0, 0), 1)

        # Ecuacion parametrica para la elipse
        elipseX = int(center_x + a * np.cos(t))
        elipseY = int(center_y + b * np.sin(t))

        cv2.circle(img, (elipseX, elipseY), 1, (153, 0, 153), 1)
        cv2.circle(img, (elipseX-2, elipseY-2), 1, (0, 0, 0), 1)

        # Ecuacion parametrica para el Hipocicloide
        hipocicloideX = int(center_x + (a - b) * np.cos(t) + b * np.cos((a - b) / b * t))
        hipocicloideY = int(center_y + (a - b) * np.sin(t) - b * np.sin((a - b) / b * t))

        cv2.circle(img, (hipocicloideX, hipocicloideY), 1, (0, 255, 255), 1)
        cv2.circle(img, (hipocicloideX-2, hipocicloideY-2), 1, (0, 0, 0), 1)

        # Ecuacion parametrica para la Epicloide
        epicloideX = int(center_x + (a + b) * np.cos(t) - b * np.cos((a + b) / b * t))
        epicloideY = int(center_y + (a + b) * np.sin(t) - b * np.sin((a + b) / b * t))

        cv2.circle(img, (epicloideX, epicloideY), 1, (0, 76, 153), 1)
        cv2.circle(img, (epicloideX-2, epicloideY-2), 1, (0, 0, 0), 1)

        # Ecuacion parametrica para la Cardiode
        cardioideX = int(center_x + a * (1 - np.cos(t)) * np.cos(t))
        cardioideY = int(center_y + a * (1 - np.cos(t)) * np.sin(t))

        cv2.circle(img, (cardioideX, cardioideY), 1, (0, 234, 0), 1)
        cv2.circle(img, (cardioideX-2, cardioideY-2), 1, (0, 0, 0), 1)

        # Ecuacion parametrica para la Rosa de Cuatro Petalos
        rosaCPX = int(center_x + a * np.cos(2 * t) * np.cos(t))
        rosaCPY = int(center_y + a * np.cos(2 * t) * np.sin(t))

        cv2.circle(img, (rosaCPX, rosaCPY), 1, (0, 0, 153), 1)
        cv2.circle(img, (rosaCPX-2, rosaCPY-2), 1, (0, 0, 0), 1)

    cv2.imshow("Parametric Animation", img)
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    theta += theta_increment

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()