# Weatherometer
# A Twitter Weather bot for Vancouver
# Author: Edison Suen

# -*- coding: utf-8 -*-
import tweepy
import requests
import time

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
FORECAST_SECRET_KEY = ''
LATITUDE = ''
LONGITUDE = ''

# message = "I am alive."
# api.update_status(status=message)

# Sample API Call
# https://api.darksky.net/forecast/c2a71f07851cebbadd94168ef1cef705/37.8267,-122.4233
url = 'https://api.darksky.net/forecast/{}/{},{}?units=si'.format(FORECAST_SECRET_KEY, LATITUDE, LONGITUDE)
headers = {'User-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
while True:
	response = requests.get(url,headers=headers)
	if response.status_code != 200:
		print("Error: ", r.status_code)
	print(url)
	data = response.json()
	# print(data)
	temperature = str(int(round(data['currently']['temperature'])))
	daily = data['daily']['summary']
	hourly = data['hourly']['summary']
	# print(temperature)
	# print(daily)
	# print(hourly)
	message = "It's currently " + temperature + u'\N{DEGREE SIGN}' + "C. " + hourly + " " + daily
	if len(message) > 140:
		message = "It's currently " + temperature + u'\N{DEGREE SIGN}' + "C. " + daily
	# print(message)
	api.update_status(status=message)
	time.sleep(14400)