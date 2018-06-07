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


# A fim de manter a proporção da imagem, necessitamos de 
# calcular a proporção entre a nova imagem e a imagem antiga
# Para uma nova imagem de 150px de largura, tem-se:
r = 150.0 / image.shape[1]              # image.shape retorna [altura, largura, canais]
dim = (150, int(image.shape[0] * r))    # dimensão da nova imagem

# Realiza o redimensionamento
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
windowName = "Resized"
cv2.imshow(windowName, resized)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Analogamnte, fixando a altura da imagem
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
windowName = "Resized"
cv2.imshow(windowName, resized)
cv2.waitKey(0)
cv2.destroyWindow(windowName)