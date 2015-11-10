__author__ = 'Sebastian'
from gopigo import *
import time

#global variables begin here
STOP_DISTANCE = 50
#global variables begin here

class Pigo:

    ######
    ###### BASIC STATUS AND METHODS
    ######
    #key value dictionary for basic state of pigo
    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175, 'dist' : 100}

    def __init__(self):
        print "I am alive with the magic of friendship!"
        self.status['dist'] = us_dist(15)

    #named after method stop() in GoPiGo lib
    def stop(self):
        self.status['ismoving'] = False
        for x in range(3):
            time.sleep(0.1)
            stop()
            print "ERROR 01: Can't stop"

    #named after method fwd() in GoPiGo lib
    def fwd(self):
        self.status['ismoving'] = True
        for x in range(3):
            time.sleep(0.1)
            fwd()
            print "ERROR 02: Can't move fwd"

    #used to tell the main loop to keep going unless something goes wrong
    def keepGoing(self):
        if self.status['dist'] < STOP_DISTANCE:
            return False
        elif volt() > 14 or volt() < 6:
            print "WARNING 02: Voltage outside of safe range: " + str(volt())
            return False
        else:
            return True

    #used to check distance
    def checkDistance(self):
        self.status['dist'] = us_dist(15)
        print "dist = " + str(self.status['dist']) + " mm"

    ######
    ###### COMPLEX METHODS
    ######

    def dance(self):
        print "MONEY"
        self.spin()
        self.shuffle()


######
###### MAIN APP STARTS HERE
######
pinkie = Pigo()

while pinkie.keepGoing():
    pinkie.checkDistance()
    pinkie.fwd()
    time.sleep(2)
    pinkie.stop()

pinkie.stop()
del pinkie