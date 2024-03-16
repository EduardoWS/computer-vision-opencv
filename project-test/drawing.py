import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 para a primeira câmera, 1 para a segunda, etc.

while(True):
    ret, frame = cap.read() # Captura um frame
    width = int(cap.get(3)) # Largura do frame
    height = int(cap.get(4)) # Altura do frame
    
    # img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5) # Desenha uma linha
    # img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5) # Desenha uma linha
    # img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5) # Desenha um retângulo
    # img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1) # Desenha um círculo
    font = cv2.FONT_HERSHEY_SIMPLEX # Define a fonte
    img = cv2.putText(frame, 'Edu is fine!', (250, 250), font, 2, (0, 255, 0), 5, cv2.LINE_AA) # Adiciona texto
    
    cv2.imshow('frame', img) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Fecha a janela ao pressionar a tecla 'q'
        break
    
cap.release() # Libera a câmera
cv2.destroyAllWindows() # Fecha todas as janelas abertas