import cv2

img = cv2.imread('assets/gato1.jpeg', -1) # 0 para escala de cinza, -1 para colorido e 1 para incluir transparência
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Redimensionar a imagem
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # Rotacionar a imagem
# espelhar imagem
img = cv2.flip(img, 1) # 0 para espelhar verticalmente, 1 para espelhar horizontalmente e -1 para ambos

cv2.imwrite('assets/new_image.jpg', img) # Salvar a imagem

cv2.imshow('image', img)
cv2.waitKey(0) # 0 para esperar indefinidamente
cv2.destroyAllWindows()


