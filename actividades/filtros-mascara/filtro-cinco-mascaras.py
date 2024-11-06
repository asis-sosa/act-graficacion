import cv2 
# import numpy as np

# Cargar las diferentes máscaras
mascara1 = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-mascara\sombrero-cowboy.webp", cv2.IMREAD_UNCHANGED)
mascara2 = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-mascara\oreja-derecha.webp", cv2.IMREAD_UNCHANGED)
mascara3 = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-mascara\barba-cafe.png", cv2.IMREAD_UNCHANGED)
mascara4 = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-mascara\oreja-izquierda.webp", cv2.IMREAD_UNCHANGED)
mascara5 = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-mascara\mascara-carnaval.png", cv2.IMREAD_UNCHANGED)

face_cascade = cv2.CascadeClassifier(r"D:\Sexto Semestre\Graficacion\filtros-mascara\haarcascade_frontalface_alt2.xml")
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostros = face_cascade.detectMultiScale(frame_gris, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))

    for (x, y, w, h) in rostros:
        y_offset = 50
        y = max(0, y - y_offset)

        ancho_extra = 80  
        x = max(0, x - ancho_extra // 2)  
        w = w + ancho_extra 

        # Crear posiciones para cinco máscaras
        posiciones = [
            (x, y - h // 2, mascara1),  # Arriba
            (x + w // 2, y, mascara2),  # Derecha
            (x, y + h, mascara3),       # Abajo
            (x - w // 2, y, mascara4),  # Izquierda
            (x, y, mascara5)            # Centro
        ]

        for (px, py, mascara) in posiciones:
            mascara_redimensionada = cv2.resize(mascara, (w, h))
            mascara_rgb = mascara_redimensionada[:, :, :3]
            mascara_alpha = mascara_redimensionada[:, :, 3]

            roi = frame[py:py+h, px:px+w]

            if roi.shape[0] != h or roi.shape[1] != w:
                continue

            mascara_alpha_inv = cv2.bitwise_not(mascara_alpha)
            fondo = cv2.bitwise_and(roi, roi, mask=mascara_alpha_inv)
            mascara_fg = cv2.bitwise_and(mascara_rgb, mascara_rgb, mask=mascara_alpha)
            resultado = cv2.add(fondo, mascara_fg)

            frame[py:py+h, px:px+w] = resultado

    cv2.imshow('Video con mascara', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
