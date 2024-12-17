import numpy as np
import cv2 as cv

# Tamaño deseado para la ventana y la imagen transparente
window_width = 600
window_height = 600

# Captura el video desde la cámara web
cap = cv.VideoCapture(0)

# Parámetros para el algoritmo de Lucas-Kanade
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

# Lee el primer fotograma del video
ret, first_frame = cap.read()
if not ret:
    raise ValueError("No se pudo leer el primer fotograma del video.")

# Redimensiona el primer fotograma para que coincida con el tamaño de la ventana
first_frame = cv.resize(first_frame, (window_width, window_height))

# Convierte el primer fotograma a escala de grises
prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)

# Posición inicial de las bolas
ball_pos_1 = np.array([[150, 300]], dtype=np.float32)
ball_pos_2 = np.array([[250, 300]], dtype=np.float32)
ball_pos_3 = np.array([[350, 300]], dtype=np.float32)

# Añade una dimensión adicional para cumplir con los requisitos de entrada de calcOpticalFlowPyrLK
ball_pos_1 = ball_pos_1[:, np.newaxis, :]
ball_pos_2 = ball_pos_2[:, np.newaxis, :]
ball_pos_3 = ball_pos_3[:, np.newaxis, :]

# Copia de las posiciones de las bolas para dibujar los círculos
circulo_pos_1 = ball_pos_1.copy()
circulo_pos_2 = ball_pos_2.copy()
circulo_pos_3 = ball_pos_3.copy()

# Cargar la imagen de fondo
background_img = cv.imread(r'D:\Sexto Semestre\Graficacion\proyecto-final\imagen-referencia.jpg', cv.IMREAD_UNCHANGED)
if background_img is None:
    raise ValueError("No se pudo cargar la imagen. Verifica la ruta del archivo.")

# Escalamiento de la imagen en una tercera parte (1/3)
scale_factor = 1/3
background_img = cv.resize(background_img, None, fx=scale_factor, fy=scale_factor)

angle = 0  # Ángulo inicial de rotación

# Escalas mínimas y máximas para las transformaciones
min_scale = 1/5  # Escala mínima
max_scale = 1/2  # Escala máxima

while True:
    # Lee un nuevo fotograma del video
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensiona el fotograma para que coincida con el tamaño de la ventana
    frame = cv.resize(frame, (window_width, window_height))

    # Convierte el fotograma a escala de grises
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Calcula el nuevo posicionamiento de las bolas usando el flujo óptico de Lucas-Kanade
    new_ball_pos_1, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos_1, None, **lk_params)
    new_ball_pos_2, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos_2, None, **lk_params)
    new_ball_pos_3, st, err = cv.calcOpticalFlowPyrLK(prev_gray, gray_frame, ball_pos_3, None, **lk_params)

    if new_ball_pos_1 is not None:
        # Actualiza la posición de la primera bola si se ha calculado correctamente
        ball_pos_1 = new_ball_pos_1
        circulo_pos_1 = new_ball_pos_1

    if new_ball_pos_2 is not None:
        # Actualiza la posición de la segunda bola si se ha calculado correctamente
        dx = new_ball_pos_2[0, 0, 0] - ball_pos_2[0, 0, 0]
        ball_pos_2 = new_ball_pos_2
        circulo_pos_2 = new_ball_pos_2

        # Determina la dirección del movimiento de la segunda bola para rotar la imagen
        if abs(dx) > 2:  # Añadimos una sensibilidad mínima para evitar pequeños cambios
            if dx > 0:
                angle -= 2  # Rotar en sentido del reloj
            elif dx < 0:
                angle += 2  # Rotar en sentido contrario al reloj

    if new_ball_pos_3 is not None:
        # Determina la dirección de movimiento de la bola para escalar la imagen
        dy = new_ball_pos_3[0, 0, 1] - ball_pos_3[0, 0, 1]
        if dy > 0:
            scale_factor += 0.01  # Aumentar tamaño
        elif dy < 0:
            scale_factor -= 0.01  # Reducir tamaño

        # Limitar el factor de escala
        scale_factor = min(max_scale, max(min_scale, scale_factor))

        # Redimensionar la imagen de fondo
        background_img_scaled = cv.resize(background_img, None, fx=scale_factor, fy=scale_factor)

        # Actualiza la posición de la bola si se ha calculado correctamente
        ball_pos_3 = new_ball_pos_3
        circulo_pos_3 = new_ball_pos_3

    # Obtiene las coordenadas de las bolas
    a1, b1 = circulo_pos_1.ravel()
    a2, b2 = circulo_pos_2.ravel()
    a3, b3 = circulo_pos_3.ravel()

    # Dibuja círculos en las nuevas posiciones de las bolas
    frame = cv.circle(frame, (int(a1), int(b1)), 20, (0, 255, 0), -1)  # Bola número 1 color Verde
    frame = cv.circle(frame, (int(a2), int(b2)), 20, (0, 0, 255), -1)  # Bola número 2 color Azul
    frame = cv.circle(frame, (int(a3), int(b3)), 20, (255, 0, 0), -1)  # Bola número 3 color Rojo

    # Convertir el ángulo a radianes para la matriz de rotación
    rotation_matrix = cv.getRotationMatrix2D((background_img_scaled.shape[1] // 2, background_img_scaled.shape[0] // 2), angle, 1)
    rotated_img = cv.warpAffine(background_img_scaled, rotation_matrix, (background_img_scaled.shape[1], background_img_scaled.shape[0]))

    # Crear una imagen de fondo transparente del tamaño del fotograma
    transparent_background = np.zeros((window_width, window_height, 3), dtype=np.uint8)

    # Calcular la posición centrada de la imagen de fondo escalada y rotada
    offset_x = (window_width - rotated_img.shape[1]) // 2
    offset_y = (window_height - rotated_img.shape[0]) // 2

    # Calcular el desplazamiento para mover la imagen de fondo
    offset_x = int(a1) - rotated_img.shape[1] // 2
    offset_y = int(b1) - rotated_img.shape[0] // 2

    # Asegurarse de que los índices estén dentro de los límites de transparent_background y rotated_img
    y1, y2 = max(0, offset_y), min(transparent_background.shape[0], offset_y + rotated_img.shape[0])
    x1, x2 = max(0, offset_x), min(transparent_background.shape[1], offset_x + rotated_img.shape[1])
    bg_y1, bg_y2 = max(0, -offset_y), max(0, -offset_y) + (y2 - y1)
    bg_x1, bg_x2 = max(0, -offset_x), max(0, -offset_x) + (x2 - x1)

    if rotated_img.shape[0] > 0 and rotated_img.shape[1] > 0:
        transparent_background[y1:y2, x1:x2] = rotated_img[bg_y1:bg_y2, bg_x1:bg_x2]

    # Mostrar el video original con las pelotas en movimiento
    cv.imshow('Controles de Movimiento con Flujo Optico', frame)

    # Mostrar la imagen en el espacio transparente separado
    cv.imshow('Transformaciones en la imagen', transparent_background)

    # Actualiza el fotograma previo con el fotograma actual
    prev_gray = gray_frame.copy()

    # Si se presiona la tecla 'Esc', se sale del bucle
    if cv.waitKey(30) & 0xFF == 27:
        break

# Libera la captura de video y destruye todas las ventanas
cap.release()
cv.destroyAllWindows()
