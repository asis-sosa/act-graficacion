# FILTRO DE CONVOLUCIÓN CON ESCALADO
import cv2
import numpy as np
import time

# Cargar la imagen en escala de grises
img = cv2.imread(r"D:\Sexto Semestre\Graficacion\filtros-convolucion\gyuw4.png", cv2.IMREAD_GRAYSCALE)

# Obtener dimensiones de la imagen original
rows, cols = img.shape

# Crear una nueva imagen donde cada píxel esté rodeado de ceros
new_img = np.zeros((2 * rows - 1, 2 * cols - 1), dtype=img.dtype)

# Rellenar la nueva imagen con los píxeles originales
new_img[::2, ::2] = img

# Medir el tiempo de ejecución
start_time = time.time()

# Definir el kernel de convolución (como el que mencionaste)
id_kernel = np.array([[-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]])

# Aplicar la convolución
flt_img = cv2.filter2D(src=new_img, ddepth=-1, kernel=id_kernel)

# Calcular el tiempo de ejecución
execution_time = time.time() - start_time
print('Tiempo de ejecución: {} segundos'.format(execution_time))

# Mostrar la imagen resultante
cv2.imshow('Imagen sin kernel aplicado', new_img)
cv2.imshow('Imagen con kernel aplicado', flt_img)
cv2.waitKey(0)
cv2.destroyAllWindows()