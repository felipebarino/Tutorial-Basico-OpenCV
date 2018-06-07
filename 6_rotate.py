# Importa as bibliotecas
from __future__ import print_function
import numpy as np
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "trex.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)
windowName = "Original"
cv2.imshow(windowName, image)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Obter a altura e largura da imagem
(h, w) = image.shape[:2]
# Calcular o centro da imagem
center = (w // 2, h // 2)

# Rotacionar a imagem por 45 degrees
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
windowName = "Rotated by 45 Degrees"
cv2.imshow(windowName, rotated)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Rotacionar a imagem por -90 degrees
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
windowName = "Rotated by -90 Degrees"
cv2.imshow(windowName, rotated)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

