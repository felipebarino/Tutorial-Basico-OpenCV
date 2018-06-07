# Importa as bibliotecas
from __future__ import print_function
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "trex.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)

# Imagens são importadas como arrays NumPy
# A origem (0, 0) é o canto superior esquerdo da imagem
(b, g, r) = image[0, 0]
# Mostra o valor dos três canais em (y=0, x=0)
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Da mesma forma que podemos acessar um pixel, 
# podemos trocar seu valor, configurando ele para vermelho
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# Pode-se pegar um intervalo do array NumPy, usando o operador ':'
# O canto superior esquerdo com 100px é dado abaixo
corner = image[0:100, 0:100]

# Mostra a imagem em uma janela nomeada pela variável: windowName
windowName = "Corner"
cv2.imshow(windowName, corner)
# Espera pelo clique de uma tecla qualquer, quando na janela windowName
cv2.waitKey(0)
# Destrói a janela windowName
cv2.destroyWindow(windowName)

# Analogamente ao dito anteriormente, pode-se setar 
# todos esses valores para um dado valor, verde por exemplo
image[0:100, 0:100] = (0, 255, 0)

# Mostra a imagem em uma janela nomeada pela variável: windowName
windowName = "New image"
cv2.imshow(windowName, image)
# Espera pelo clique de uma tecla qualquer, quando na janela windowName
cv2.waitKey(0)
# Destrói a janela windowName
cv2.destroyWindow(windowName)