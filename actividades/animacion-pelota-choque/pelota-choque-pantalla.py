import numpy as np
import cv2

# Dimensiones de la ventana
width, height = 640, 480

# Crear una ventana
cv2.namedWindow('Pelota en Movimiento')

# Posición inicial de la pelota
ball_pos = np.array([width // 2, height // 2])
# Velocidad inicial de la pelota
ball_velocity = np.array([5, 5])
# Radio de la pelota
ball_radius = 20

while True:
    # Crear una imagen negra
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Actualizar la posición de la pelota
    ball_pos += ball_velocity

    # Verificar colisiones con los límites de la ventana
    if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > width:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > height:
        ball_velocity[1] = -ball_velocity[1]

    # Dibujar la pelota
    cv2.circle(frame, tuple(ball_pos), ball_radius, (0, 255, 0), -1)

    # Mostrar la imagen
    cv2.imshow('Pelota en Movimiento', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()