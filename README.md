# MONITORING HYDROPONIC PLANTS BY TWITTER


## PROJECT DESCRIPTION:
The main purpose of the project is to build a device that will automatically, in a given time interval, send tweets containing a photo and information on climatic factors (temperature and humidity) of the hydroponic garden IKEA VAXER.


## NECESSARY EQUIPMENT:

### Hardware components:
1) Raspberry Pi (I've used RPi 3 model B+)
2) Raspberry Pi camera
3) DHT11 sensor
4) Male female jumper wires
5) IKEA VAXER hydroponics kit

### Software used for the project:
1) Raspberry Pi Raspbian
2) Tweepy
3) Twitter (you have to create an account for which you want to send information)
quirements and stages


## REQUIREMENTS AND STAGES
You'll need to install the python, picamera, tweepy and DHT11 sensor. First of all you should connect your Raspberry Pi with DHT11 sensor and Raspberry Pi Camera and make sure everything works. 


#### DHT11 - Scheme
Once we have all the equipment connected, we can go to software installation. At the beginning, we will test whether our sensor works. For this purpose, we collect the ready code from Githuba.

```
git clone git: //github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
cd Adafruit-Raspberry-Pi-Python-Code / Adafruit_DHT_Driver
sudo ./Adafruit_DHT 11 4
```

"11" is a DHT sensor model (there are also models 22), and "4" is a GPIO pin to which we have our sensor connected. Sometimes we have to enter this command several times before measurements appear. This is due to the fact that the sensor itself checks the temperature and humidity from time to time. If we see the current temperature and air humidity, it means that everything works and we can go further.


### Raspberry Pi Camera
I recommend to use official tutorial available [here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera)
 


### Tweepy
Now he have working camera and sensor so it's time to set Twitter API which is necessary to use Tweepy. 

The API is free to use, but you have to have a Twitter account and to register your application in order to get access to the API. I recommend to create a new account, because I think your friends and other followers donÕt what to see your tweet with your "hydroponic garden" :simple_smile:

**TIP:** If you use Twitter on your phone, follow your "project account". That allows you to receive tweets on your phone (through your private Twitter account). 

Start by going to apps.twitter.com. Create a new app by completing the required fields. After that you could generate a Consumer key, Consumer secret, Access token, and Access token secret. You'll need these four keys to connect to your Twitter account from your Python code.

**WARNING:** Don't share these keys with anyone, as they can be used without the account's password. 

Now we need to install the tweepy module, which allows as to create connection between python program and Twitter. 

```
sudo pip install tweepy
```

## CODE
Make sure that you've installed python3 and your default terminal settings are set to use python3 (that's common mistake!)

Make a copy of the code or download hydroponic_plants.py. 

As you can see there is no loop included in the code. To run this program periodically and at fixed intervals you could use Crontab (tool builded on Unix systems) or use Cron GUI - The Gnome-Schedule. To install this run:

```
sudo apt-get install gnome-schedule
```

Then you can launch the program Scheduled Tasks from the main menu. And that is it!


## AT THE END
I hope that this program will be useful for you all. Feel free to use it, develop and add other sensor. There is no limit :) 

I will be working on it by adding some new features so stay tuned and furthermore HAVE FUN!

