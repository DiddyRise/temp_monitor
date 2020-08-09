import Adafruit_DHT
import sys
import time
from datetime import datetime

########################################
#
#Change your stuff here!
#
# set your sensor
#Adafruit_DHT.AM2302 / Adafruit_DHT.11 / Adafruit_DHT.22
sensor = Adafruit_DHT.AM2302
# Set the GPIO pin (e.g. GPIO17 = 17)
pin = 17
#
# Set the time in seconds between each probe - Please note that that the minimum is 2 seconds
set_time = 300
#
########################################


f = open("results.csv", "w")
f.write("Time,Temperature,Humidity\n")
f.close
while True:
    time.sleep(set_time)
    f = open("results.csv", "a")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
         result = (str(current_time)  + "," + str(round(temperature, 2)) + "," + str(round(humidity, 2))) 
         print(result)
         f.write(result + "\n")
         f.close
    else:
        print("0")
        
