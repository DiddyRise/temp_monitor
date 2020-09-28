import Adafruit_DHT
import sys
import time
from datetime import datetime
import os

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
value_format = 'comma' #set delimiter (comma / dot)
########################################

# some random stack overflow thingy to make sure cron uses the correct directory, don't ask how or why :) 
os.chdir(sys.path[0])

# preparing the csv file
# if file exists, do nothing, else create the file
if os.path.exists('./results.csv'):
    print("results.csv file exists, skipping creation!")
else:
    print("results.csv file not found, creating...!")
    f = open("results.csv", "w")
    f.write("Time;Temperature;Humidity\n")
    f.close

# initializes date variable, prints start date
today = datetime.today().date()
print("Start Date: " + str(today))

# main loop
while True:

    #checks for date change & renames file if new date is found
    time.sleep(set_time)
    if datetime.today().date() != today:
        os.rename("results.csv","results_" + str(today) + ".csv")
        f = open("results.csv", "w")
        f.write("Time;Temperature;Humidity\n")
        f.close
        today = datetime.today().date() #sets the new date to the current date
    else:
        pass


    f = open("results.csv", "a")
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d - %H:%M") # Change the date output here
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        #check for delimiter setting
        if value_format == 'comma':
         result = (str(current_time)  + ";" + str(round(temperature, 2)).replace('.',',') + ";" + str(round(humidity, 2)).replace('.',',')) 
        else:
         result = (str(current_time) + ";" + str(round(temperature, 2)) + ";" + str(round(humidity, 2)))
    
        print(result) # this can be turned off, if no terminal output is required
        f.write(result + "\n")
        f.close
    
    else:
        print("0")
# end of main loop        
