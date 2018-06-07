# Importa as bibliotecas
from __future__ import print_function
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

# Cortar uma imagem é simples, com o uso do operador ':' do NumPy
#	inicioY:finalY, inicioX:finalX
cropped = image[30:120 , 240:335]
windowName = "Face"
cv2.imshow(windowName, cropped)
cv2.waitKey(0)
cv2.destroyWindow(windowName)