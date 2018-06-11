# Importa as bibliotecas
import numpy as np
import cv2

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "lego.jpg"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)

# Aplica filtro bilateral
blurred = 	cv2.bilateralFilter(image, 9, 41, 41)

# transforma o espaço de copres, HSV é mais indicado
# para segmentação de cores
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

 # Definir os limites inferiores e superiores da cor 
 # que se deseja segmentar
lower_blue = np.array([20,80,80])
upper_blue = np.array([33,255,255])

# Obter uma máscara com valores 1 apenas onde as cores da imagem original
# estão no intervalo dado pelas variáveis acima
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Aplica um "filtro" à máscaram contraindo os contornos obtidos e depois
# os expandindo, dessa forma os pequenos objetos (ruído) desaparecem
mask = cv2.erode(mask, (10, 10))
mask = cv2.dilate(mask, (10,10))

# Aplica a másca à imagem original
res = cv2.bitwise_and(image, image, mask=mask)

# Mostrar o resultado
windowName = "Segmentação"
cv2.imshow(windowName, res)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

# Converter para escala de cinza
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

# Retirar ruídos
blurred = cv2.GaussianBlur(gray, (9, 9), 0)
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

# Desenhar os contornos encontrados, em verde
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (1, 1, 1), 2)
windowName = "Coins"
cv2.imshow(windowName, coins)
cv2.waitKey(0)
cv2.destroyWindow(windowName)