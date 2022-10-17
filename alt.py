from picamera import PiCamera
import shutil
import subprocess
from datetime import datetime
from time import sleep
import cv2


def takepicture(resolution):
	timestamp = datetime.now()
	timestamp = timestamp.strftime("%d %m %Y, %H %M %S")
	print('timestamp:', timestamp)
	filename = "/home/pi/Desktop/Bilder/" + str(timestamp)
	#filename = filename.replace(":", "")
	#filename = filename.replace(".", "")
	# filename=filename.replace(" ","")
	camera = PiCamera(resolution = resolution, framerate_range=(1.0/6.0, 30)  )
	camera.iso =800
	# Wait for the automatic gain control to settle
	sleep(1.5)
	# Now fix the values
	camera.shutter_speed = 750000
	camera.exposure_mode = 'auto'
	#camera.awb_mode = 'off'
	#camera.awb_gains = g
	 #	 camera.start_preview()
	 # filename=filename.replace(" ","")
	filename=filename+"expo:"+str(camera.exposure_compensation)
	filename = filename +"analog_g:" + str(camera.analog_gain)
	filename += "digital_g:" + str(camera.digital_gain)
	#filename = filename.replace("/", "_")
	print("filename", filename)
	camera.capture((filename + ".jpg"))
	camera.close()
	sleepietime = wielangschlafen(filename)
	print("Picture taken")
	return sleepietime
def wielangschlafen(filename):
	img_load = cv2.imread(filename+".jpg")
	gray_image = cv2.cvtColor(img_load,cv2.COLOR_RGB2GRAY)
	mean=cv2.mean(gray_image)
	if mean[0]<7:
		sleeptime = 3600
	elif mean[0]<10:
		sleeptime = 1800
	elif mean [0]<50:
		sleeptime = 60
	return sleeptime
def wlancheck():
	if "Wireless" not in str(subprocess.check_output("lsusb")):
		print(subprocess.check_output("echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind"))
		try:
			f= open("/home/pi/Desktop/logs/wifideact","a")
			f.write(str(datetime.now) +"deact \n")
			f.close()
		except:
			print("fehler beim Wlan aus datei schreiben")
	else:
		print("wlan bleibt an")
		try:
			f=open("/home/pi/Desktop/logs/wifideact","a")
			f.write(str(datetime.now)+"aktiv \n")
			f.close()
		except:
			print("fehler beim wlan an Datei schreiben")

if __name__ == '__main__':
	####### PARM
	resolution = 2592, 1944  # or 1280, 720
	crontab_running = True
	###Parm
	#Wlancheck() #bleib muss noch debugged werden
	if crontab_running == True:
		while shutil.disk_usage("/")[2] > 10 * 6:
			sleeptime = takepicture(resolution)
			print("waiting", sleeptime, "s")
			sleep(sleeptime)
			print(shutil.disk_usage("/")[2])
	else:
			print("Programm wird beendet")
