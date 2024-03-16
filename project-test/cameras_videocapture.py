import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 para a primeira câmera, 1 para a segunda, etc.

while(True):
    ret, frame = cap.read() # Captura um frame
    width = int(cap.get(3)) # Largura do frame
    height = int(cap.get(4)) # Altura do frame
    
    image = np.zeros(frame.shape, np.uint8) # Cria uma imagem preta
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # Redimensiona o frame
    
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # Rotaciona o frame
    image[height//2:, :width//2] = cv2.flip(smaller_frame, 1) # Espelha o frame
    
    gray_small_frame = cv2.cvtColor(smaller_frame, cv2.COLOR_BGR2GRAY) # Converte para escala de cinza
    gray_small_frame_colored = cv2.cvtColor(gray_small_frame, cv2.COLOR_GRAY2BGR) # Converte de volta para BGR para ter 3 canais
    image[:height//2, width//2:] = gray_small_frame_colored # Agora isso deve funcionar sem erro
    
    image[height//2:, width//2:] = smaller_frame
    
    cv2.imshow('frame', image) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Fecha a janela ao pressionar a tecla 'q'
        break
    
cap.release() # Libera a câmera
cv2.destroyAllWindows() # Fecha todas as janelas abertas