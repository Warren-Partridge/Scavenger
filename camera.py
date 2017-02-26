from picamera import PiCamera
from time import sleep

#camera = PiCamera()
#camera.resolution = (1024,768)
#camera.framerate = 15

def takePicture():

    try:
        camera = PiCamera()
        camera.resolution = (2592, 1944)
        camera.framerate = 15

        camera.start_preview()
        #sleep(1)
        camera.capture('/home/pi/Desktop/image.jpg')
    
        camera.stop_preview()
        camera.close()
    except:
        print( 'Exception - try again')

#takePicture()

