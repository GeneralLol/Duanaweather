from subprocess import Popen
import time, sys#, termios, tty, os	#Those commented libs are used for keystroke recognition. 

set_time_interval    = 1				#Interval between every update of time
set_weather_interval = 200				#Interval between every update of weather
#The WeatherModule will be called once in 20 mins, the TimeModule will be called every second. The Display Module will be started at the start of the program according to the arguments specified and refresh itself. 

def WeatherModule():
	Popen(['python3 WeatherModule.py'], shell = True)

def TimeModule():
	Popen(['python3 TimeModule.py'], shell = True)

def VirtualDisplay():
	Popen(['python3 VirtualDisplay.py'], shell = True)


#This chunk is to decide which display module to pull up. 
args = sys.argv
sig = True

#If number of arguments is wrong, skip the while loop and end everything. 
if len(args) > 2: 
	sig = False
	print('Wrong arguments. Please use -h to get help.')
	
elif args[1] == '-vd': 		#If argument is -vd pull up Virtual Display Module
	VirtualDisplay()
	sig = True
	
elif args[1] == '-h':		#If argument is -h then pull up help file. 
	help_file_raw = open('Help', 'r')
	help_file     = help_file_raw.read()
	print(help_file)
	sig = False
	
else: 
	print('Wrong arguments. Please use -h to get help.')
	sig = False

#Those two variables store the interval between the last and the current trigger of the time and weather modules. 
interval_time 	 = 0
interval_weather = 0

#Those two variables are used to caculate separately the time interval for weather update and time update
timeCache    = time.clock_gettime(time.CLOCK_REALTIME)//1	
weatherCache = time.clock_gettime(time.CLOCK_REALTIME)//1

if sig: 
	print('Please visit https://www.wunderground.com/?apiref=c68c74f9a26733fa to provide me with free API access. Thanks!')
	print('Ctrl+C to quit the program.')
	#Update the time and weather before displaying
	TimeModule()
	WeatherModule()

while sig:
	#print('While True Started')			#Print is for plebs/debugging
	current_time = time.clock_gettime(time.CLOCK_REALTIME)//1
	#interval_time records the current time from the last trigger of TimeModule. 
	#interval_weather records the current time from the last trigger of WeatherModule. 
	interval_time    = current_time-timeCache
	interval_weather = current_time-weatherCache
	#key = getch()
	
	#This if clause is triggered once every second to update the time, resets the time counter and updates the time
	if (interval_time >= set_time_interval):
		#print('Time Updated')				#Print is for plebs/debugging
		TimeModule()
		interval_time = 0
		timeCache = current_time
		
	#This if clause is triggered once every 200 secs to update the weather, then resets the weather counter. 
	if (interval_weather >= set_weather_interval): 
		#print('Weather Updated')			#Print is for plebs/debugging
		WeatherModule()
		interval_weather = 0
		weatherCache = current_time
	
	time.sleep(0.5)				#halt for half a second to save sys resources
