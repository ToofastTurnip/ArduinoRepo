from picamera import PiCamera
from time import sleep

camera = PiCamera()

# camera.rotation = 180
# Uncomment that^ if the image is upside down
camera.start_preview()
sleep(10)
# Sleep take arg is seconds, so that's 10 seconds
camera.stop_preview()


# camera.start_preview()
# for i in range(5):
#     sleep(5)
#     camera.capture('/home/pi/Desktop/image%s.jpg' % i)
# camera.stop_preview()
# Take 5 pictures (one every 5 seconds)^

# camera.start_preview()
# camera.start_recording('/home/pi/video.h264')
# sleep(10)
# camera.stop_recording()
# camera.stop_preview()
# Then playback the video with the terminal icon on pi editor interface and enter 'omxplayer video.h264'

# Camera has a ton of other methods too like resolution, framerate, and annotate_text (there's filters too)
