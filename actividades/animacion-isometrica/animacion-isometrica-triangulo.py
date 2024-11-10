import cv2
import numpy as np

WIDTH, HEIGHT = 800, 600

# Definir los vértices del triángulo
vertices = np.array([
    [-1, -1, -1],
    [1, -1, -1],
    [0, 1, -1],
    [-2, 1, -1]
])

# Definir los bordes del triángulo
edges = [
    (0, 1), (1, 2),
    (0, 2), (2, 3),
    (0, 3)
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