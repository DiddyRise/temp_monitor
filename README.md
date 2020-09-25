# temp_monitor


This is a simple script to read room temperature & humidity and write it to a csv file for further investigation. The script requires the depricated ADAfruit_Python_DHT library to be installed.

https://github.com/adafruit/Adafruit_Python_DHT

## Installation
This little script is pretty simple to install. Just follow these steps and you should be good to go!


### Install python
```
sudo apt-get update && sudo apt-get install python3
```


### Install git
```
sudo apt-get install git
```

### Install PIP & Adafruit_DHT
```
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
```

### Clone repository
- change directory to a path of your choise
```
cd /your/path/here
```
- clone the repository
```
git clone https://github.com/DiddyRise/temp_monitor
```


## Usage
- The script is called with:
```
python3 temp.py
```
- The result.csv file is located in the same folder

### Variables
- sensor: Lets you change the sensor. There are currently 3 options: 
`````
Adafruit_DHT.DHT11
Adafruit_DHT.DHT22
Adafruit_DHT.AM2302
`````

- pin: Lets you specify the GPIO Pin that your sensor signal is connected to (e.g. GPIO17)

- set_time: Time between sensor readings in seconds

- value_format: You can choose between comma and dot for the value format.



