import urllib.request
import json

import os, sys

city_file  = open('City' , 'r')
state_file = open('State', 'r')
city = city_file.read()
state = state_file.read()
url = 'http://api.wunderground.com/api/386a8e8ab04d7748/conditions/q/'+state+'/'+city+'.json'

response = urllib.request.urlopen(url)
	
res = json.load(response)

if 'error' in res['response'].keys():
	os.remove('Weather')
	f = open('Weather', 'w+')
	f.close()
	print('Error. Please check the city and state settings. Ctrl+C to quit.')
	os.remove('runFlag')
	f = open('runFlag', 'w+')
	f.write('0')
	f.close()
	sys.exit()

obs_rst = res['current_observation']			#Fetches the observation results as a large dictionary

def location(): 
	endString = city + ' ' + state				#Processes two strings into one for final output
	return endString
#location() works and returns a string that looks like "San Fran CA". 

weather	= obs_rst['weather']					#Fetches weather as a string
temp 	= str(obs_rst['temp_c']) + ' degrees Celsius'			#Fetches temperature, outputs something like "20 degrees Celsius"
loc		= location()							#Fetches location

final_str = loc + '\n' + weather + '\n' + temp
#Makes the final string, outputs something like "Manchester NH, Mostly Cloudy, 4.7℃". 
os.remove('Weather')
f = open('Weather', 'w+')
f.write(final_str)
