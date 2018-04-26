# Project_Oracle
## Objective: 
To create a piece of software that is able to pull weather information and display it through the serial port of a Raspberry Pi. 

## Setup: 
  1. Setup the Serial communication on the Raspberry Pi
  2. Connect the Serial display to the Raspberry Pi. 
  3. Download the project files into one folder. 
  4. Get into the folder directory in the terminal. 
  5. Run python3 Duanaweather -h to see the help docs. 
 
 ## End Result: 
 The program should display date, time, weather and temperature to the display hooked up. 
 
 ## OS Support: 
 Currently this project only supports Ubuntu x86-64. It is made and tested on Ubuntu. Other distros have not been tested. Windows will kinda work if you have the environmental variables set right. Everything is still manual though. 

 ## Current Issues:
 There is still no adaptations for a physical display. Also the Virtual Display is made using pygame, which takes a lot of sys resources. Considering about switching to PyQt. 
 
 The Calendar Module is still work in progress. 
