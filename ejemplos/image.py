#import numpy as np
#import cv2 as cv
#img = np.ones((500, 500), dtype=np.uint8)
#cv.imshow('image', img)
#cv.waitKey()
#cv.destroyAllWindows()

#import cv2 as cv 
#import numpy as np 
#img = cv.imread(r"C:\Users\bobe-\OneDrive\Documentos\logo_ITM.png",0) 
#h,w = img.shape[:2] 
#img2 = np.zeros((h*2, w*2, 1) , dtype = "uint8") 
#print("Valores " + str(img.shape[:2])) 
#for i in range(h):
#    for j in range(w): img2[i*2,j*2]=img[i,j]
#cv.imshow('imagen', img) 
#cv.imshow('imagen2', img2) 
#cv.waitKey(0) 
#cv.destroyAllWindows()

''' Diferentes pruebas. Prueba 1. Crea una matriz de 500x500 con valores aleatorios
entre 0 y 255 en escalas de grises
import numpy as np
import cv2 as cv
img = np.random.randint(0, 256, (500, 500), dtype=np.uint8)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()'''

''' Diferentes pruebas. Prueba 2. Crea una matriz de 500x500 con 3 canales (RGB), cada
uno con valores aleatorios entre 0 y 255
import numpy as np
import cv2 as cv
img_color = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)
cv.imshow('image_color', img_color)
cv.waitKey(0)
cv.destroyAllWindows()'''

''' Diferentes pruebas. Prueba 3. Crea una matriz donde los valores aumentan de 0 a 499
en cada fila, creando un degrada horizontal'''
import numpy as np
import cv2 as cv
img_gradient = np.tile(np.arange(500, dtype=np.uint8), (500, 1))
cv.imshow('image_gradient', img_gradient)
cv.waitKey(0)
cv.destroyAllWindows()