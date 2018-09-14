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

# To disable the led so there is no indication that the camera is on:
# in terminal: sudo nano /boot/config.txt
# add to end of file: disable_camera_led=1
# ctrl+o then ctrl+x to save and close
# in terminal: sudo reboot

# Future plans: upload files automatically to dropbox in the event that the pi is physically compromised
