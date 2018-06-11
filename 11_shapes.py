# Importa as bibliotecas
import numpy as np
import cv2

def detect(c):
    # A princípio não se conhece o objeto
    shape = "indefinido"
    peri = cv2.arcLength(c, True)
    # aproxima a borda do contorno por um polígono
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    # testa pelo número de vértices da aproxiomação
    if len(approx) == 3:
        shape = "triangulo"
 
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        # se os lados têm a mesma proporção, é um quadrado 
        if ar >= 0.95 and ar <= 1.05:
            shape = "quadrado"  
        else:
            shape ="retangulo"

    elif len(approx) == 5:
        shape = "pentagono"
        
    elif len(approx) == 6:
        shape = "hexagono"
 
    # para polígonos de muitos lado, assumir um círculo
    else:
        shape = "circulo"
 
    return shape

# Nome do arquivo de imagem a ler e caminho dele, a partir do atual
fileName = "shape.jpg"
path = "Images/" + fileName

# Carrega a imagem
image = cv2.imread(path)

# transforma o espaço de copres, HSV é mais indicado
# para segmentação de cores
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica filtro gaussiano
blurred = 	cv2.GaussianBlur(gray, (13, 13), 0)

# Intervalos para retirar o fundo
lower = 0
upper = 220

# Obter uma máscara com valores 1 apenas onde as cores da imagem original
# estão no intervalo dado pelas variáveis acima
mask = cv2.inRange(blurred, lower, upper)

# Aplica um "filtro" à máscaram contraindo os contornos obtidos e depois
# os expandindo, dessa forma os pequenos objetos (ruído) desaparecem
mask = cv2.erode(mask, (10, 10))
mask = cv2.dilate(mask, (10,10))

# Aplica a másca à imagem original
res = cv2.bitwise_and(image, image, mask=mask)

# Encontrar os contornos da imagem
# OBS: cv2.findContours destrói a imagem de 
# entrada, se for reutilizar: faça cópia
(_, cnts, _) = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    # calcula o centro do contorno
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]))
    cY = int((M["m01"] / M["m00"]))
    
    # chama a função de detectar
    shape = detect(c)
    
    # escreve o polígono detectado
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 
                .5, (0, 0, 0), 2)

windowName = "Detecção"
cv2.imshow(windowName, image)
cv2.waitKey(0)
cv2.destroyWindow(windowName)

