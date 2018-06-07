# Importa as bibliotecas
from __future__ import print_function
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "trex.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
windowName = "Gray"
cv2.imshow(windowName, gray)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Converte a imagem para HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
windowName = "HSV"
cv2.imshow(windowName, hsv)
cv2.waitKey(0)
cv2.destroyWindow(windowName)
