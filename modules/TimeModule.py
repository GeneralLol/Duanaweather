from datetime import datetime
from os import remove

datetime = str(datetime.now())			#Fetching date & time in a long big string
date = datetime[:10]					#Separates date and time
time = datetime[11:]
time =     time[:8 ]					#Gets rid of the milliseconds

finalString = date + '\n' + time		#Produces a final string that looks like 2018-03-06\n16:12:21


remove('data/Time')							#Removes the previous time file and makes a new one
f = open('data/Time', 'w+')
f.write(finalString)					#Writes the final string into the cache file


#print(date)					#Prints for debugging
#print(time)
