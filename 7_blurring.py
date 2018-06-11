# Importa as bibliotecas
import numpy as np
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "wave.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)
windowName = "Original"
cv2.imshow(windowName, image)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# blur: filtro média móvel
# pega a mádia em um quadrado de número ímpar na imagem
# e seta o pixel central como essa média
# Quanto maior o tamanho do quadrado, maior o "blur"
blurred = np.hstack([
	cv2.blur(image, (3, 3)),
	cv2.blur(image, (5, 5)),
	cv2.blur(image, (7, 7))])
windowName = "Averaged"
cv2.imshow(windowName, blurred)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# gaussianBlur: filtro gaussiano
# os elementos da matriz (kernel), usada para a convolução
# com a imagem original, segue uma gaussiana 2d 
# Quanto maior o tamanho da matriz, maior o "blur"
# Quanto maior o desvio padrão da gaussiana, maior o "blur"
blurred = np.hstack([
	cv2.GaussianBlur(image, (3, 3), 0),
	cv2.GaussianBlur(image, (5, 5), 0),
	cv2.GaussianBlur(image, (7, 7), 0)])
windowName = "Gaussian"
cv2.imshow(windowName, blurred)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Além de remover o ruído da imagem, os filtros acima tiram 
# nididez em arestas. Para manter essa nitidez o filtro bilateral 
# pode ser utilizado. 
blurred = np.hstack([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter(image, 7, 31, 31),
	cv2.bilateralFilter(image, 9, 41, 41)])
windowName = "Bilateral"
cv2.imshow(windowName, blurred)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Importa a mesma imagem com ruído
fileName = "wave_noise.png"
path = "Images/" + fileName

# Carrega a imagem com ru´pido gaussiano
image_noise = cv2.imread(path)

# Filtro gaussiano
blurred = cv2.GaussianBlur(image_noise, (5, 5), 0)

img2show = np.hstack([image_noise, blurred])

windowName = "Comparacao"
cv2.imshow(windowName, img2show)
cv2.waitKey(0)
cv2.destroyWindow(windowName)


