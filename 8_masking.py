# Importa as bibliotecas
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

# Máscara é utilizada para focarmos em uma região
# normalmente para obter informações de algum objeto
# Uma máscara possui o mesmo tamanho da imagem original, 
# mas possui apenas dois valores de cor: 0 ou 255
# Ao aplicar uma operação binária AND, pixel a pixel, 
# entre a máscara e a imagem original, os pixel da 
# imagem original são mantidos para as regiões onde 
# a máscara é 255 e os pixel nas posições onde a 
# máscara é 0 são ignorados

# Uma máscara com um quadrado 150X150px no centro da
# imagem pode ser criado com:
mask = np.zeros(image.shape[:2], dtype = "uint8")
# calcula o centro
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
# faz o quadrado em questão, setando a 255
# o parâmetro -1 diz que todo o interior vai ser prenchido
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75 , cY + 75), 255, -1)
windowName = "Mask"
cv2.imshow(windowName, mask)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Aplica a operação AND bit a bit entre a imagem
# e a máscara
masked = cv2.bitwise_and(image, image, mask = mask)
windowName = "Mask & Image"
cv2.imshow(windowName, masked)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Agora uma máscara circular
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
windowName = "Mask"
cv2.imshow(windowName, mask)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Aplicar
masked = cv2.bitwise_and(image, image, mask = mask)
windowName = "Mask & Image"
cv2.imshow(windowName, masked)
cv2.waitKey(0)
cv2.destroyWindow(windowName)