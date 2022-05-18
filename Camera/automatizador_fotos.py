from picamera import PiCamera
from time import sleep

#Constroi o objeto da câmera
camera = PiCamera ()

#inicia a visualização da câmera. O Alpha = 200 da uma opacidade para ver através da gravação
#e poder acompanhar caso ocorra algum erro. Pode ser setado de 0 a 255.
camera.start_preview (alpha=200)
sleep(30)
camera.stop_preview()
#percorre o array e a cada 3s salva uma foto no diretório
sleep(5)
camera.start_preview(alpha=200)

for i in range(4):
    sleep(10)
    for j in range(50):
        sleep (2)
        camera.capture('/home/mathezzz/Imagens/Camera Rasp/foto' + str(i) + str(j) + '.jpg')
#Para a visualização da câmera
camera.stop_preview ()