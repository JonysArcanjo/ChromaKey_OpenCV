import cv2
import numpy as np

# Carrega as bibliotecas necessárias.
cap_webcam = cv2.VideoCapture('data/shakira_modnet_com.mp4')
cap_fundo = cv2.VideoCapture('data/fundo_canva.mp4')


# Loop principal.
while True:
    # Lê um quadro de cada vídeo.
    ret_webcam, frame_webcam = cap_webcam.read()
   
    ret_fundo, frame_fundo = cap_fundo.read()
   
    # Verifica se os vídeos terminaram.
    # Se sim, termina o loop.
    if not ret_webcam or not ret_fundo:
        break

    # Define os limites da cor verde em RGB.
    # Esses limites serão usados para criar a máscara.
    
    lower_green = np.array([60, 138, 60], dtype=np.uint8)
    upper_green = np.array([180, 255, 180], dtype=np.uint8)   

    # Cria uma máscara com os pixels que estão dentro da faixa de cor verde.
    mask = cv2.inRange(frame_webcam, lower_green, upper_green)
    
    # Usa a máscara para extrair os pixels do fundo que correspondem ao fundo verde da webcam.
    fundo_background = cv2.bitwise_and(frame_fundo, frame_fundo, mask=mask)
    
    # Inverte a máscara para obter os pixels que não estão na faixa de cor verde.
    mask_inv = np.invert(mask)
    
    # Usa a máscara invertida para extrair os pixels da webcam que não são verdes.
    webcam_foreground = cv2.bitwise_and(frame_webcam, frame_webcam, mask=mask_inv)
    
    # Combina as imagens resultantes.
    result = cv2.addWeighted(fundo_background, 1, webcam_foreground, 1, 0)
    
    # Exibe a imagem resultante.
    cv2.imshow("Resultado", result)

    # Aguarda por um evento de teclado pressionado durante 1 milissegundo.
    # Se a tecla pressionada for 'q', o loop é interrompido.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap_webcam.release()
cap_fundo.release()
cv2.destroyAllWindows()
