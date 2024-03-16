import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 para a primeira câmera, 1 para a segunda, etc.

while(True):
    ret, frame = cap.read() # Captura um frame
    width = int(cap.get(3)) # Largura do frame
    height = int(cap.get(4)) # Altura do frame
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Converte para o espaço de cores HSV
    lower_blue = np.array([90, 50, 50]) # Define o limite inferior da cor azul
    upper_blue = np.array([130, 255, 255]) # Define o limite superior da cor azul
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # Cria uma máscara para a cor azul
    result = cv2.bitwise_and(frame, frame, mask=mask) # Aplica a máscara à imagem original
    
    cv2.imshow('frame', result) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Fecha a janela ao pressionar a tecla 'q'
        break
    
cap.release() # Libera a câmera
cv2.destroyAllWindows() # Fecha todas as janelas abertas