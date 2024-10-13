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

# Posición inicial del personaje
character_pos = np.array([width // 4, height // 4])
# Tamaño del personaje
character_size = 30

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

    # Calcular la distancia entre la pelota y el personaje
    distance = np.linalg.norm(ball_pos - character_pos)

    # Si la pelota está cerca del personaje, mover el personaje en la dirección opuesta
    if distance < 130:
        direction = character_pos - ball_pos
        direction = direction / np.linalg.norm(direction)  # Normalizar el vector de dirección
        direction = direction.astype(np.int64) # Convertir direccion a int64
        character_pos += direction * 20  # Mover el personaje

    # Asegurarse de que el personaje no salga de los límites de la ventana
    character_pos = np.clip(character_pos, [character_size // 2, character_size // 2], [width - character_size // 2, height - character_size // 2])

    # Dibujar el personaje
    cv2.rectangle(frame, (character_pos[0] - character_size // 2, character_pos[1] - character_size // 2),
                  (character_pos[0] + character_size // 2, character_pos[1] + character_size // 2), (255, 0, 0), -1)

    # Mostrar la imagen
    cv2.imshow('Pelota en Movimiento', frame)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Cerrar todas las ventanas
cv2.destroyAllWindows()