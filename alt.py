from picamera import PiCamera
import shutil
from datetime import datetime
from pathlib import Path
from time import sleep


def takepicture(resolution):
    camera = PiCamera(resolution=(resolution),sensor_mode=1 )
    camera.iso =800
    # Wait for the automatic gain control to settle
    sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    timestamp = datetime.now()
    print('timestamp:', timestamp)
 #   camera.start_preview()
    filename = "/home/pi/Desktop/Bilder/" + str(timestamp)
    filename = filename.replace(":", "")
    filename = filename.replace(".", "")
    # filename=filename.replace(" ","")
    camera.capture((filename + ".jpg"))
#    camera.stop_preview()
    print("Picture taken")
    camera.close()
    return


if __name__ == '__main__':
    ####### PARM
    resolution = 2592, 1944  # or 1280, 720
    crontab_running = True
    ###Parm


    if crontab_running == True:
        while shutil.disk_usage("/")[2] > 10 * 6:
            takepicture(resolution)
            print("waiting 50 s")
            sleep(30)
            print(shutil.disk_usage("/")[2])


    else:
        print("Programm wird beendet")
    print_hi('PyCharm')
