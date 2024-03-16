import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 para a primeira câmera, 1 para a segunda, etc.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Carrega o classificador de faces
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') # Carrega o classificador de olhos

while(True):
    ret, frame = cap.read() # Captura um frame
    width = int(cap.get(3)) # Largura do frame
    height = int(cap.get(4)) # Altura do frame
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converte o frame para tons de cinza
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Detecta as faces no frame
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Fecha a janela ao pressionar a tecla 'q'
        break
    
cap.release() # Libera a câmera
cv2.destroyAllWindows() # Fecha todas as janelas abertas