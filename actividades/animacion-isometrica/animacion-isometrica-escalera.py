import cv2
import numpy as np

WIDTH, HEIGHT = 900, 700

# Definir los vértices de la escalera
vertices = np.array([
    [0, -4, 2], #0
    [0, -1, 2], #1
    [1, 2.5, 0], #2
    [4, 0.5, 1], #3
    [4, -0.5, 1], #4
    [3, -1, 1], #5
    [3, -2, 1], #6
    [2, -2.5, 1], #7
    [2, -3.5, 1], #8
    [0, -3, 0], #9
    [0, -2.5, 1], #10
    [0, -1.5, 1], #11
    [0, 0, 0], #12
    [0, 1, 0], #13
    [1, 1.5, 0], #14
])

# Definir los bordes de la escalera
edges = [
    (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0), # Exterior de la escalera
    (0, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 2), # Interior de la escalera
    (14, 4), (13, 5), (12, 6), (11, 7), (10, 8) # Intersecciones entre escalones
]

def project_isometric(vertex):
    x, y, z = vertex
    x2D = x - z
    y2D = (x + 2 * y + z) / 2
    return int(x2D * 100 + WIDTH / 2), int(-y2D * 100 + HEIGHT / 2)

cv2.namedWindow("Triángulo Isométrico")

while True:
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    for edge in edges:
        pt1 = project_isometric(vertices[edge[0]])
        pt2 = project_isometric(vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

    cv2.imshow("Triángulo Isométrico", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()