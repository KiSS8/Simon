#!/usr/bin/env python3
import sys
import tweepy as tp
import Adafruit_DHT
from subprocess import call
from datetime import datetime

# taking photo
i = datetime.now()
now = i.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
cmd = 'raspistill -t 500 -w 1024 -h 768 -rot 180 -o /home/pi/' + photo_name 
call ([cmd], shell=True)

# taking data from sensor DHT11
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

if humidity is not None and temperature is not None:
   data_dht11 = ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
   print ('Failed to get data. Try again!')

# Data from Twitter API to authorization 
consumer_key = "put here your consumer key"
consumer_secret = "put here your consumer secret"
access_token = "put here your access token"
access_secret = "put here your access secret"

# Authorization process, using the keys and tokens
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Creation of the actual interface, using authentication
api = tp.API(auth)

# Send the tweet with photo and data from sensor
photo_path = '/home/pi/' + photo_name
status = 'Hydroponic plants monitoring status: \n' + data_dht11 + '\n Date: ' + i.strftime('%Y/%m/%d %H:%M:%S') 
api.update_with_media(photo_path, status=status)
