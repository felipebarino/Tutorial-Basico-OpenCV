# Importa as bibliotecas
import numpy as np
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "coins.png"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)
windowName = "Original"
cv2.imshow(windowName, image)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Retirar ruídos
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
windowName = "Blurred"
cv2.imshow(windowName, blurred)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Detectar bordas com o algoritmo Canny
# basicamente um passa alta 2d
edged = cv2.Canny(blurred, 30, 150)
windowName = "Edges"
cv2.imshow(windowName, edged)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Encontrar os contornos da imagem
# OBS: cv2.findContours destrói a imagem de 
# entrada, se for reutilizar: faça cópia
(_, cnts, _) = cv2.findContours(edged.copy(), 
             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Qual o tamanho do retorno, cnts? Quantos contorno foram encontrados
print("I count {} coins in this image".format(len(cnts)))

# Desenhar os contornos encontrados, em verde
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
windowName = "Coins"
cv2.imshow(windowName, coins)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Para cada contorno
for (i, c) in enumerate(cnts):
    # Calcula o retângulo que engloba o contorno em questão
    (x, y, w, h) = cv2.boundingRect(c)
    
    # Com o resultado do retângulo dado por (x, y, w, h)
    # Podemos cortar a moeda da imagem, com o operador ':'
    coin = image[y:y+h, x:x+w]
    
    windowName = "Coin " + str(i+1)    
    cv2.imshow(windowName, coin)
    cv2.waitKey(0)
    cv2.destroyWindow(windowName)

	# Just for fun, let's construct a mask for the coin by finding
	# The minumum enclosing circle of the contour
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    masked = cv2.bitwise_and(coin, coin, mask = mask)
    
    windowName = " Masked Coin " + str(i+1)
    cv2.imshow(windowName, masked)
    cv2.waitKey(0)
    cv2.destroyWindow(windowName)