import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def draw_triangle(vertices):
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()

def main():
    # Inicializar pygame y la ventana de OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    # Generar el triángulo de Pascal
    n = 10
    triangle = pascal_triangle(n)

    # Configurar los vértices usando el triángulo de Pascal
    vertices = []
    for i in range(n):
        for j in range(len(triangle[i])):
            x = (i + 1) * 100
            y = triangle[i][j] * 50
            vertices.append((x, y))

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar triángulos
        for i in range(0, len(vertices) - 2, 3):
            draw_triangle(vertices[i:i + 3])

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()