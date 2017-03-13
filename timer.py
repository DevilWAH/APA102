#imports
import time
import string
import random
import readchar
import math


#setting up the three letters that player will type
string.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L1 = random.choice(string.letters)
L2 = random.choice(string.letters)
L3 = random.choice(string.letters)

#instruction message
print ""
print "Get Ready to type"
print "The letters you will need to type are " + L1 + " " +  L2 + " "  + L3 
print "The Timer will start as soon as you hit the space bar and stop when you corectly type the last letter" 
print ""

#set all user varibles to false
Uspace = None
U1 = None
U2 = None
U3 = None


#wait for player to press space to start
while not (Uspace == " "):
	print("----READY HIT SPACE TO START!!!!----")
	Uspace = readchar.readkey()

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
