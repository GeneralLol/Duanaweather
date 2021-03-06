#from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime, time
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_dir = dir + '/modules/secret.json'

#Decide whether to execute this module from the Runflag file
runFlag_dir  = dir + '/cache/runFlag'
runFlag_file = open(runFlag_dir, 'r')
runFlag = int(runFlag_file.read())
runFlag_file.close()
if not runFlag:
    quit()

credentials_dir = dir + '/modules/credentials.json'
# Setup the Calendar API
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage(credentials_dir)
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(secret_dir, SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
now_ref = time.time()
calendarid = 'i7vs7cuh27t4kvh0k517tnk3m8fjms11@import.calendar.google.com'
events_result = service.events().list(calendarId=calendarid, timeMin=now,
                                      maxResults=60, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])
blocks = [None]

if not events:
    quit()

index = 0
refresh_index = 0
start = [None] * 60
refresh_flag = False
refresh_counter = True
for event in events:
    start[index] = event['start'].get('dateTime', event['start'].get('date'))
    #If there are 20 chars in start, it's a class. Otherwise it's a homework.
    if len(start[index]) == 20:
        blocks.append(event['summary'])
        refresh_flag = True
    if refresh_flag and refresh_counter:
        refresh_index = index
        refresh_counter = False
    index += 1
blocks.pop(0)


#Final process that isolates the block information from the entire string
next_block = ''
flag = False
for i in blocks[1]:
    if i == '(':
        flag = True
    if i == ')':
        flag == False
    if flag:
        next_block += i
length = len(next_block)
next_block = next_block[1:]
next_block = next_block[:length-2]

#Write the block info into the cache file
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = dir + '/data/Block'
refresh_dir = dir + '/cache/CalendarRefresh'
try:
    os.remove(data_dir)
    os.remove(refresh_dir)
except:
    pass
utc_time = datetime.datetime.strptime(start[refresh_index+1], "%Y-%m-%dT%H:%M:%SZ")
epoch = datetime.datetime.utcfromtimestamp(0)
secs_ref = str((utc_time-epoch).total_seconds())
f = open(data_dir, 'w')
f.write(next_block)
f.close()
f = open(refresh_dir, 'w')
f.write(secs_ref)
quit()
