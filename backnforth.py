#!/usr/bin/env python


import spidev
import time
from random import randint

#Set up the SPI pins and system
spi = spidev.SpiDev()
spi.open(0,1)
spi.max_speed_hz=8000000

#number of LED
NumLED = 56


# set up varibles for indervidual LED and string that will  be sent to Strip
# Indivual LEDs can be changed be writing to LED[x]
 
LED = []
LEDs = []


for i in range(0 , NumLED):
	LED.append([0xE1, 0x00, 0x00, 0x00])
## Set up some varibels so we can easly send start from and clear frame

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



# Test write to blank all write a patten and then after 2 seconds turn the strip off
resp = spi.xfer2(Start + Blankall + EndFrame)

#rainbow colours
#brightness is E0 / 1110 0000 / 224 (the start for frame) + 0 - 31 
colour = [[Mid, 0, 0, 255],[Mid, 0, 127, 255],[Mid, 0, 255, 255],[Mid, 0, 255, 0],[Mid, 255, 0, 0],[Mid, 130, 0, 75],[Mid, 211, 0, 148]]


led = 0

for i in range(0, 7):
	for y in range(0, 8):
		LED[led] = colour[i]
		led = led + 1	

#LEDs = []
#for x in range (0, NumLED):
#        LEDs = LEDs + LED[x]


LEDs = [item for sublist in LED for item in sublist]

resp = spi.xfer2(Start + LEDs + EndFrame)





#for y in range(0, 10000):

try:
	print "Press Ctrl-C to Exit"
	while True:
		tempLED = LED[0]
        	for x in range(0, NumLED-1):
                	LED[x] = LED[x+1]
        	LED[NumLED-1] = tempLED
	        LEDs = []


#        	for x in range (0, NumLED):
#                	LEDs = LEDs + LED[x]

		LEDs = [item for sublist in LED for item in sublist]
        	resp = spi.xfer2(Start + LEDs + EndFrame)
        	time.sleep(0.01)
        
except KeyboardInterrupt:
    pass


resp = spi.xfer2(Start + Blankall + EndFrame)	

