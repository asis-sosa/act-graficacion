import numpy as np
import cv2

width, height = 561, 544

pixel_matrix = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        # Fila 1
        if y >= 0 and y <= 17:
            if (x >= 0 and x <= 238) or (x >= 340 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 238 and x <= 340):
                pixel_matrix[y, x] = [0, 0, 255]

        # Fila 2
        if y >= 17 and y <= 34:
            if (x >= 0 and x <= 221) or (x >= 357 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [0, 0, 255]

        # Fila 3
        if y >= 34 and y <= 51:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if(x >= 306 and x <= 323):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 4
        if y >= 51 and y <= 68:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [64, 64, 64]
            if(x >= 323 and x <= 340):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 5
        if y >= 68 and y <= 85:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 6
        if y >= 85 and y <= 102:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 7
        if y >= 102 and y <= 119:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 8
        if y >= 119 and y <= 136:
            if (x >= 0 and x <= 170) or (x >= 408 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 170 and x <= 187) or (x >= 391 and x <= 408):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 9
        if y >= 136 and y <= 153:
            if (x >= 0 and x <= 170) or (x >= 408 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 170 and x <= 187) or (x >= 391 and x <= 408):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 10
        if y >= 153 and y <= 170:
            if (x >= 0 and x <= 170) or (x >= 408 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 170 and x <= 187) or (x >= 391 and x <= 408):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 11
        if y >= 170 and y <= 187:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 12
        if y >= 187 and y <= 204:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 13
        if y >= 204 and y <= 221:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 14
        if y >= 221 and y <= 238:
            if (x >= 0 and x <= 221) or (x >= 357 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [64, 64, 64]
        
        # Fila 15
        if y >= 238 and y <= 255:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [32, 32, 32]

        # Fila 16
        if y >= 255 and y <= 272:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 238) or (x >= 340 and x <= 374):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [32, 32, 32]

        # Fila 17
        if y >= 272 and y <= 289:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [32, 32, 32]

        # Fila 18
        if y >= 289 and y <= 306:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 238 and x <= 272) or (x >= 306 and x <= 340):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [32, 32, 32]

        # Fila 19
        if y >= 306 and y <= 323:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [32, 32, 32]

        # Fila 20
        if y >= 323 and y <= 340:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 238 and x <= 272) or (x >= 306 and x <= 340):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 21
        if y >= 340 and y <= 357:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 22
        if y >= 357 and y <= 374:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 238) or (x >= 340 and x <= 374):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 23
        if y >= 374 and y <= 391:
            if (x >= 0 and x <= 187) or (x >= 391 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 187 and x <= 204) or (x >= 374 and x <= 391):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 204 and x <= 238) or (x >= 272 and x <= 306) or (x >= 340 and x <= 374):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 238 and x <= 272) or (x >= 306 and x <= 340):
                pixel_matrix[y, x] = [0, 0, 0]

        # Fila 24
        if y >= 391 and y <= 408:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 238 and x <= 340):
                pixel_matrix[y, x] = [96, 96, 96]

        # Fila 25
        if y >= 408 and y <= 425:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 255 and x <= 357) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]

        # Fila 26
        if y >= 425 and y <= 442:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 27
        if y >= 442 and y <= 459:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 28
        if y >= 459 and y <= 476:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 29
        if y >= 476 and y <= 493:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 30
        if y >= 493 and y <= 510:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 238) or (x >= 340 and x <= 357):
                pixel_matrix[y, x] = [96, 96, 96]
            if (x >= 238 and x <= 255) or (x >= 323 and x <= 340):
                pixel_matrix[y, x] = [64, 64, 64]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 31
        if y >= 510 and y <= 527:
            if (x >= 0 and x <= 204) or (x >= 374 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 204 and x <= 221) or (x >= 357 and x <= 374):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [32, 32, 32]
            if (x >= 255 and x <= 272) or (x >= 306 and x <= 323):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 272 and x <= 306):
                pixel_matrix[y, x] = [255, 255, 255]

        # Fila 32
        if y >= 527 and y <= 544:
            if (x >= 0 and x <= 221) or (x >= 357 and x <= 561):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 221 and x <= 255) or (x >= 323 and x <= 357):
                pixel_matrix[y, x] = [0, 0, 255]
            if (x >= 255 and x <= 323):
                pixel_matrix[y, x] = [255, 255, 255]

cv2.imshow('Pixel Art', pixel_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
