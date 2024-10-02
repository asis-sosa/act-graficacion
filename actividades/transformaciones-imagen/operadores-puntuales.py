import numpy as np
import matplotlib.pyplot as plt

imagen = plt.imread('pixel_art_cer0.jpg')

# Crear el negativo
negativo = 255 - imagen

# Convertir a escala de grises
gris = np.dot(imagen[..., :3], [0.2989, 0.5870, 0.1140])

# Definir un umbral
umbral = 128

# Aplicar umbralización
umbralizada = (gris > umbral) * 255

# Definir un factor de brillo
brillo = 50

# Ajustar el brillo
imagen_brillo = np.clip(imagen + brillo, 0, 255)

# Definir un factor de contraste
contraste = 1.5

# Ajustar el contraste
imagen_contraste = np.clip(128 + contraste * (imagen - 128), 0, 255)

# Crear una figura con subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Mostrar la imagen original
axs[0, 0].imshow(imagen, cmap='gray')
axs[0, 0].set_title('Original')
axs[0, 0].axis('off')

# Mostrar la imagen negativa
axs[0, 1].imshow(negativo, cmap='gray')
axs[0, 1].set_title('Negativo')
axs[0, 1].axis('off')

# Mostrar la imagen en escala de grises
axs[0, 2].imshow(gris, cmap='gray')
axs[0, 2].set_title('Escala de Grises')
axs[0, 2].axis('off')

# Mostrar la imagen umbralizada
axs[1, 0].imshow(umbralizada, cmap='gray')
axs[1, 0].set_title('Umbralización')
axs[1, 0].axis('off')

# Mostrar la imagen con ajuste de brillo
axs[1, 1].imshow(imagen_brillo)
axs[1, 1].set_title('Ajuste de Brillo')
axs[1, 1].axis('off')

# Mostrar la imagen con ajuste de contraste
axs[1, 2].imshow(imagen_contraste)
axs[1, 2].set_title('Ajuste de Contraste')
axs[1, 2].axis('off')

plt.tight_layout()
plt.show()