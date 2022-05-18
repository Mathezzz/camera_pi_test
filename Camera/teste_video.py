from picamera import PiCamera
from time import sleep

#Constroi o objeto da câmera
camera = PiCamera ()

#inicia a visualização da câmera. O Alpha = 200 da uma opacidade para ver através da gravação
#e poder acompanhar caso ocorra algum erro. Pode ser setado de 0 a 255.
camera.start_preview (alpha=200)
#aguarda 5s antes de iniciar a gravação
sleep(5)
#Começa a gravar o arquivo que será salvo no diretório destino abaixo.
camera.start_recording('/home/mathezzz/Vídeos/Camera rasp/video.h264')
sleep(10) #Grava por 10s
camera.stop_recording() #Para a gravação

#Para a visualização da câmera
camera.stop_preview ()
