from picamera import PiCamera
from time import sleep

#Constroi o objeto da câmera
camera = PiCamera ()

#inicia a visualização da câmera. O Alpha = 200 da uma opacidade para ver através da gravação
#e poder acompanhar caso ocorra algum erro. Pode ser setado de 0 a 255.
camera.start_preview (alpha=200)
#percorre o array e a cada 3s salva uma foto no diretório
for i in range(10):
    sleep (3)
    #print(i)
    camera.capture('/home/mathezzz/Imagens/Camera Rasp/foto' + str(i) + '.jpg')

#Para a visualização da câmera
camera.stop_preview ()