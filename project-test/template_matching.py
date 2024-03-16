import numpy as np
import cv2

img = cv2.imread('assets/soccer_practice.jpg', 0) # Carrega a imagem
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # Redimensiona a imagem
template = cv2.imread('assets/shoe.PNG', 0) # Carrega o template
template = cv2.resize(template, (0, 0), fx=0.5, fy=0.5) # Redimensiona o template
h, w = template.shape # Obtém a altura e a largura do template

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] # Métodos de comparação

for method in methods:
    img2 = img.copy() # Cria uma cópia da imagem
    
    result = cv2.matchTemplate(img2, template, method) # Compara a imagem com o template
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) # Obtém os valores mínimo e máximo e suas posições
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    
    cv2.rectangle(img2, location, (location[0] + w, location[1] + h), 255, 2) # Desenha um retângulo
    cv2.imshow('Match', img2) # Mostra a imagem
    cv2.waitKey(0) # Fecha a janela ao pressionar qualquer tecla
    cv2.destroyAllWindows() # Fecha todas as janelas abertas
    
