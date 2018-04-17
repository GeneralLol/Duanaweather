import pygame, os, sys
from pygame.locals import *
from time import sleep

#Actual program
pygame.init()
font = pygame.font.SysFont('roboto', 40)
#x and y are dimensions of the window. 
x = 500
y = 309
screen = pygame.display.set_mode((x,y))	#Sets the size

#Sets the window. Working. 
def set_window():
	window_caption = 'Duanaweather'
	pygame.display.set_caption(window_caption)	#Sets the title
	#Sets the background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))
	
	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

#Adds the time. 
def display_time():
	
	try: 
		date_time_file = open('Time'   , 'r')
	except FileNotFoundError: 
		return
	
	date_time      = date_time_file.readlines()
	#If clause: If time file is empty(created by 'open'), skip this function. 
	if os.stat('Time').st_size == 0:
		return
		
	date = date_time[0]
	time = date_time[1]
	date = date[:10]			#Gets rid of the \n at the end of the line
	
	font = pygame.font.SysFont('roboto', 70)
	time_label = font.render(time, 1, (255, 255, 255))
	
	font = pygame.font.SysFont('roboto', 30)
	date_label = font.render(date, 1, (255, 255, 255))
	
	screen.blit(time_label, (5  , 80))
	screen.blit(date_label, (5, 5))
	
	pygame.display.flip()

def display_weather():
	
	try: 
		city_weather_file = open('Weather', 'r')
	except FileNotFoundError: 
		return
		
	city_weather      = city_weather_file.readlines()
	#If clause: If weather file is empty, skip this function. 
	if os.stat('Weather').st_size == 0:
		return
		
	city        = city_weather[0]
	city		= city   [:len(city)-1]
	weather     = city_weather[1]
	weather 	= weather[:len(weather)-1]
	temperature = city_weather[2]
	
	font = pygame.font.SysFont('roboto', 50)
	weather_label     = font.render(weather    , 1, (255, 255, 255))
	font = pygame.font.SysFont('roboto', 30)
	loc_label         = font.render(city       , 1, (255, 255, 255))
	font = pygame.font.SysFont('roboto', 30)
	temperature_label = font.render(temperature, 1, (255, 255, 255))
	
	screen.blit(weather_label    , (5  , 35 ))
	screen.blit(loc_label        , (5  , 280))
	screen.blit(temperature_label, (250, 45 ))
	
	pygame.display.flip()

def reset_window():
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((150, 150, 150))
	
	screen.blit(background, (0, 0))				#Applies the background
	pygame.display.flip()						#Refreshes the window

#Initial check to see if to run the module or not. 
flag_raw = open('runFlag')
flag = flag_raw.readlines()
flag_raw.close()
if flag[0] == '0': 
	sys.exit()

set_window()
#Try-except used to detect keystrokes and to quit the program. 
while True: 
	reset_window()
	display_time()
	display_weather()
	#Check whether the flag is still up. If flag down, end display. 
	flag_raw = open('runFlag')
	flag = flag_raw.readlines()
	flag_raw.close()
	for event in pygame.event.get(): 
		if event.type == QUIT:
			os.remove ('runFlag')
			f = open('runFlag', 'w')
			f.write('0')
			f.close()
			sys.exit()
	if flag[0] == '0':
		sys.exit()

