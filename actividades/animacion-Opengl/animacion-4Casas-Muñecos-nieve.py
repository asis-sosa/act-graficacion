import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluNewQuadric, gluSphere, gluPerspective, gluCylinder, gluLookAt
import sys

def init():
    """Configuración inicial de OpenGL"""
    glClearColor(0.5, 0.8, 1.0, 1.0)  # Fondo azul cielo
    glEnable(GL_DEPTH_TEST)           # Activar prueba de profundidad

    # Configuración de la perspectiva
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1.0, 0.1, 100.0)  # Campo de visión más amplio
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    """Dibuja el cubo (base de la casa)"""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)  # Marrón para todas las caras

    # Frente
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Atrás
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 1, 1)
    glVertex3f(-1, 1, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)

    # Arriba
    glColor3f(0.9, 0.6, 0.3)  # Color diferente para el techo
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)

    # Abajo
    glColor3f(0.6, 0.4, 0.2)  # Suelo más oscuro
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    """Dibuja el techo (pirámide)"""
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)  # Rojo brillante

    # Frente
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)

    # Atrás
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 2, 0)

    # Izquierda
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(0, 2, 0)

    # Derecha
    glVertex3f(1, 1, -1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 2, 0)
    glEnd()

def draw_ground():
    """Dibuja un plano para representar el suelo o calle"""
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)  # Gris oscuro para la calle

    # Coordenadas del plano
    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)
    glEnd()

def draw_sphere(radius=1, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, 32, 32)
    glPopMatrix()

def draw_cone(base=0.1, height=0.5, x=0, y=0, z=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(-90, 1, 0, 0)  # Orientar el cono hacia adelante
    glRotate(270, 0, 1, 0) # Girar el cono 180 grads en el eje Y
    quadric = gluNewQuadric()
    gluCylinder(quadric, base, 0, height, 32, 32)
    glPopMatrix()

def draw_snowman():
    glPushMatrix()
    glTranslatef(0.0, 0, 1.2)  # Alejar al muñeco de nieve

    # Cuerpo
    glColor3f(1, 1, 1)
    draw_sphere(0.5, -1.2, 0.4, 0)     # Base
    draw_sphere(0.375, -1.2, 0.9, 0)  # Cuerpo medio
    draw_sphere(0.25, -1.2, 1.5, 0)   # Cabeza

    # Ojos
    glColor3f(0, 0, 0)
    draw_sphere(0.07, -1.275, 1.6, 0.15)  # Ojo izquierdo
    draw_sphere(0.07, -1.125, 1.6, 0.15)   # Ojo derecho

    # Nariz (cono)
    glColor3f(1, 0.5, 0)  # Color naranja
    draw_cone(0.06, 0.2, -1.2, 1.5, 0.3)  # Nariz

    glPopMatrix()

def draw_house():
    """Dibuja una casa (base + techo + muñeco)"""
    draw_cube()  # Base de la casa
    draw_roof()  # Techo
    draw_snowman() # Muñeco de Nieve

def draw_scene():
    """Dibuja toda la escena con 4 casas"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Configuración de la cámara
    gluLookAt(10, 8, 15,  # Posición de la cámara
              0, 0, 0,    # Punto al que mira
              0, 1, 0)    # Vector hacia arriba

    # Dibujar el suelo
    draw_ground()

    # Dibujar las casas en diferentes posiciones
    positions = [
        (-5, 0, -5),  # Casa 1
        (5, 0, -5),   # Casa 2
        (-5, 0, 5),   # Casa 3
        (5, 0, 5)     # Casa 4
    ]
    for pos in positions:
        glPushMatrix()
        glTranslatef(*pos)  # Mover la casa a la posición actual
        draw_house()        # Dibujar la casa
        glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    # Inicializar GLFW
    if not glfw.init():
        sys.exit()
    
    # Crear ventana de GLFW
    width, height = 800, 600
    window = glfw.create_window(width, height, "Escena con 4 casas y muñecos", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # Bucle principal
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()