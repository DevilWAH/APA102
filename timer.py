#imports
import time
import string
import random
import readchar
import math
import spidev

### first set up SPI and LED strip ###

#Set up the SPI pins and system
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz=8000000

#number of LED
NumLED = 60


# set up varibles for indervidual LED and string that will  be sent to Strip
# Indivual LEDs can be changed be writing to LED[x]

LED = []
LEDs = []


### now set up and run the "Game" ### 

#setting up the three letters that player will type
string.letters = 'abcdefghijklmnopqrstuvwxyz'
L1 = random.choice(string.letters)
L2 = random.choice(string.letters)
L3 = random.choice(string.letters)

#instruction message
print ""
print "Get Ready to type"
print "The letters you will need to type are " + L1.upper() + " " +  L2.upper() + " "  + L3.upper() + " in lower case"
print "The Timer will start as soon as you hit the space bar and stop when you corectly type the last letter" 
print ""

#set all user varibles to false
Uspace = None
U1 = None
U2 = None
U3 = None


#wait for player to press space to start
try:
	while not (Uspace == " "):
		print("----READY HIT SPACE TO START!!!!----")
		Uspace = readchar.readkey()

except KeyboardInterrupt:
    pass

#get the start time
start = time.time()

#repeat for all the letters grabbign time stamp once each is successfuly typed. 
while not (U1 == L1):
        print("----The Next Key is " + L1 + " !!!!----")
        U1 = readchar.readkey()

L1time = time.time()


while not (U2 == L2):
        print("----The Next Key is " + L2 + " !!!!----")
        U2 = readchar.readkey()

L2time = time.time()

while not (U3 == L3):
        print("----The Next Key is " + L3 + " !!!!----")
        U3 = readchar.readkey()

L3time = time.time()

# write out the results to console
print ""
print "First Letter took ", L1time-start
print "Second Letter took ", L2time-L1time
print "Last Letter took ", L3time-L2time
print ""
print "Total time was ", L3time-start

#rounds up the total seconds to the nearest whole int and then devides by number of LED
ledint = math.ceil(L3time-start)/60
print "time devision per LED is ", ledint, " based on 60 LED's in strip"
## next work out how many LED each letter whould have
led1 = int((L1time-start)/ledint)
print "Letter one LED's = ", led1

led2 = int((L2time-L1time)/ledint)
print "Letter two LED's = ", led2

led3 = int((L3time-L2time)/ledint)
print "Letter three LED's = ", led3

otherLED = 60-(led1 + led2 + led3)

print "Padding LED's = ", otherLED


##So now we have all the data we need to output it all to the LED strip, strip will fill one LED at a time so not simply 
#flashing on but "sliding" in. 

### First we need to set up some standard VAribles

# Start frame
Start = [0x00, 0x00, 0x00, 0x00]
# Blank single LED frame
BlankS = [0xE0, 0x00, 0x00, 0x00]
#Blank all LED's 
Blankall = BlankS*(NumLED*2)
#EndFrame
EndFrame = [0]*(NumLED/2)

Low = 0xE1
Mid = 0xF0
High = 0xFF

Blue = [High, 255, 0, 0]
Green =[High, 0, 255, 0]
Red = [High, 0, 0, 255]
Purple = [Mid, 255, 0 ,255]


for i in range(0, otherLED):
	LED.append(Purple)
for i in range(0 , led3):
        LED.append(Red)
for i in range(0, led2):
	LED.append(Green)
for i in range(0, led1):
	LED.append(Blue)


try:
        print "Press Ctrl-C to Exit"
        while True:
                LEDs = [item for sublist in LED for item in sublist]
                resp = spi.xfer2(Start + LEDs + EndFrame)
                time.sleep(0.01)

except KeyboardInterrupt:
    pass


resp = spi.xfer2(Start + Blankall + EndFrame)
