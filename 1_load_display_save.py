# Importa as bibliotecas
from __future__ import print_function
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "trex.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)

# Mostrar dados básicos da imagem
# largura
print("width: {} pixels".format(image.shape[1]))
# altura
print("height: {} pixels".format(image.shape[0]))
# número de canais
print("channels: {}".format(image.shape[2]))

# Mostra a imagem em uma janela nomeada pela variável: windowName
windowName = "Image"
cv2.imshow(windowName, image)
# Espera pelo clique de uma tecla qualquer, quando na janela windowName
cv2.waitKey(0)
# Destrói a janela windowName
cv2.destroyWindow(windowName)

# Salva a imagem - OpenCV converte tipos de imagem
newName = "newimage.jpg"
path = "Images/" + newName
cv2.imwrite(path, image)