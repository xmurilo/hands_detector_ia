import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicializa a webcam
webcam = cv2.VideoCapture(0)

# Verifica se a webcam foi aberta corretamente
if not webcam.isOpened():
    print("Erro ao abrir a webcam!")
    exit()

# Inicializa o rastreador de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # Captura a imagem da webcam
    sucesso, imagem = webcam.read()

    # Verifica se a captura foi bem-sucedida
    if not sucesso:
        print("Erro ao capturar imagem da webcam!")
        break

    # Detecta as mãos no quadro
    coordenadas, imagem_maos = rastreador.findHands(imagem)
    print(coordenadas)

    # Mostra o quadro com as marcações
    cv2.imshow("Projeto - IA", imagem_maos)  # Ou use imagem, se preferir sem marcações

    # Encerra a aplicação quando qualquer tecla for pressionada
    if cv2.waitKey(1) != -1:
        break

# Libera a câmera e fecha as janelas
webcam.release()
cv2.destroyAllWindows()
