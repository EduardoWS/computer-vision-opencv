import cv2
import random

img = cv2.imread('assets/gato1.jpeg', -1) 

tag = img[300:700, 200:700] # Recortar a imagem


for i in range(300):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(155, 255), random.randint(0, 100), random.randint(155, 255)] # BGR (blue, green, red)

print(img.shape) # Dimensões da imagem (altura, largura, canais de cor)

img[100:500, 400:900] = tag # Colar a imagem recortada

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()