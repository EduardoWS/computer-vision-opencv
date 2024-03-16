import numpy as np
import cv2

img = cv2.imread('assets/chessboard.png') # Carrega a imagem
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Redimensiona a imagem
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converte para escala de cinza

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10) # Encontra os cantos da imagem
corners = np.int0(corners) # Converte para inteiros

for corner in corners:
    x, y = corner.ravel() # Achatamento
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1) # Desenha um círculo

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i].ravel())
        corner2 = tuple(corners[j].ravel())
        color = tuple(map(int, np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1) # Desenha uma linha


cv2.imshow('image', img) # Mostra a imagem original
cv2.waitKey(0) # Fecha a janela ao pressionar qualquer tecla
cv2.destroyAllWindows() # Fecha todas as janelas abertas
