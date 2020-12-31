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
- Results are saved to a date-marked file at the end of a day (e.g.: results_24.09.2020.csv)

- If you want to run this script you can use the "screen" tool

## Screen Installation and usage
- Install screen with this command:
```
sudo apt-get install screen
```
- Run tempy with this command:
```
screen python3 temp.py
```
- Move screen to the background with CTRL + A, then D
- Return to your screen session with this:
```
screen -r
```
More information here:
https://linuxize.com/post/how-to-use-linux-screen/


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


### Display on webpage
If you want to display your current data on a webpage you can follow these steps:

- Install Apache
````````
sudo apt-get install apache2
````````

- Copy the website template to the working directory of Apache2
```````
sudo mv index_template.html /var/www/html/index.html
```````

- Symlink your install directory to /var/www/html
````````
sudo ln -s /you/path/here/temp_monitor temp_monitor
````````

You should now be able to browse to the IP of your device and see measurements. Please ensure that the script is running and that your measurements are beeing recorded.
