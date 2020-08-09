import Adafruit_DHT
import sys
import time
from datetime import datetime

#now = datetime.now()

# seet your sensor
sensor = Adafruit_DHT.AM2302
# Set the GPIO pin (e.g. GPIO17 = 17)
pin = 17

f = open("results.csv", "w")
f.write("'Time','Temperature','Humidity'\n")
f.close
while True:
    time.sleep(60)
    f = open("results.csv", "a")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
         result = ("'" + str(current_time) + "'" + "," + "'" + str(round(temperature, 2)) + "'" + "," + "'" + str(round(humidity, 2)) + "'") 
         print(result)
         f.write(result + "\n")
         f.close
    else:
        print("0")
        
