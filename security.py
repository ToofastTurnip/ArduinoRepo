from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import MotionSensor

camera = PiCamera()
pir = MotionSensor(4)

while True:
    filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
    pir.wait_for_motion()
    # Code stops here until motion is detected by the motion sensor^
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()

# Then playback the video with the terminal icon on pi editor interface and enter 'omxplayer {filename}'

# Future plans: upload files automatically to dropbox in the event that the pi is physically compromised
