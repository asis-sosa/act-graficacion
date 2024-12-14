import glfw
from OpenGL.GL import *
import sys

# Variables globales para controlar la posición del cuadrado
square_x = 0.0
square_y = 0.0
speed = 0.05  # Velocidad de movimiento

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)  # Configurar un sistema de coordenadas 2D

def draw_square():
    """Dibuja un cuadrado en la posición actual"""
    global square_x, square_y

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)  # Color verde
    glPushMatrix()
    glTranslatef(square_x, square_y, 0.0)  # Trasladar el cuadrado
    glBegin(GL_QUADS)
    glVertex2f(-0.1, -0.1)
    glVertex2f(0.1, -0.1)
    glVertex2f(0.1, 0.1)
    glVertex2f(-0.1, 0.1)
    glEnd()
    glPopMatrix()
    glfw.swap_buffers(window)

def key_callback(window, key, scancode, action, mods):
    """Procesa las entradas de teclado"""
    global square_x, square_y, speed

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            square_y += speed  # Mover hacia arriba
        elif key == glfw.KEY_DOWN:
            square_y -= speed  # Mover hacia abajo
        elif key == glfw.KEY_LEFT:
            square_x -= speed  # Mover a la izquierda
        elif key == glfw.KEY_RIGHT:
            square_x += speed  # Mover a la derecha

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        print("No se pudo inicializar GLFW")
        sys.exit()

    # Crear ventana
    window = glfw.create_window(800, 600, "Prueba de Teclado", None, None)
    if not window:
        glfw.terminate()
        print("No se pudo crear la ventana")
        sys.exit()

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)  # Configurar callback de teclado
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_square()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()