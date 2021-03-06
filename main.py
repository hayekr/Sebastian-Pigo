"""
__author__ = 'Sebastian'
from gopigo import *
import time
import threading

#global variables begin here
STOP_DISTANCE = 50
VOLT = HAZARDOUS VOLTAGE#added new Global variable
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
        print "Stop"
        for x in range(5):
            time.sleep(0.1)
            stop()

    #named after method fwd() in GoPiGo lib
    def fwd(self):
        self.status['ismoving'] = True
        print "Fwd"
        for x in range(10):
            time.sleep(0.1)
            fwd()

    #used to tell the main loop to keep going unless something goes wrong
    def keepGoing(self):
        if self.status['dist'] < STOP_DISTANCE:
            print "WARNING 03: Too close to object"
            return False
            ###########
            ###Bobby- This is my change to fix your volt
            ###########
        elif volt() > 14 or volt() < 6: #check voltage and turn off robot is voltage is under 6V or above 14V
            print VOLT
            return False
            ###########
            ###Bobby- This is my change to fix your volt
            ###########
        else:
            return True

    #used to check distance
    def checkDistance(self):
        self.status['dist'] = us_dist(15)
        print "dist = " + str(self.status['dist']) + " mm"

    def threadCheckDistance(self):
        while True:
            self.status['dist'] = us_dist(15)
            print "dist = " + str(self.status['dist']) + " mm"
            if self.status['dist'] < STOP_DISTANCE:
                print "WARNING T03: Too close to object"
                self.stop()
                break

    ######
    ###### COMPLEX METHODS
    ######

    def dance(self):
        print "MONEY"
        self.spin()
        #dancer = threading.Thread(target=servoShake, args=(self))
        #dancer.start()

        self.servoShake()
        self.checkDistance()
        self.backNForth()
        self.checkDistance()
        self.strobe()
        self.checkDistance()
        self.servoShake()
        self.checkDistance()
        #dancer.join()

    def spin(self):
        time.sleep(0.1)
        set_speed(251)
        left_rot()
        time.sleep(3)

    def backNForth(self):
        for x in range(5):
            time.sleep(0.1)
            set_speed(251)
            fwd()
            time.sleep(2)
            bwd()
            time.sleep(2)

    def strobe(self):
        print "let's have a rager!"
        for x in range(7):
            led_on(1)
            time.sleep(.3)
            led_off(0)
            time.sleep(.3)
            led_off(1)
            time.sleep(.3)
            led_on(0)
            time.sleep(.3)

    def servoShake(self):
        for x in range(10):
            servo(120)
            time.sleep(2)
            servo(30)

    def servoSweep(self):
        for ang in range(20, 160, 5):
            if ang % 3 == 0:
                servo(ang)
                time.sleep(.1)
######
###### MAIN APP STARTS HERE
######
pinkie = Pigo()

while pinkie.keepGoing():
    dancer = threading.Thread(group=None, target=Pigo.threadCheckDistance, name="Swag", args=(pinkie, ), kwargs=None)
    dancer.start()
    pinkie.spin()
    dancer.join()

pinkie.stop()
del pinkie
"""

"""
__author__ = 'Sebastian'
from gopigo import *
import time
import threading

#global variables begin here
STOP_DISTANCE = 50
VOLT = "HAZARDOUS VOLTAGE"
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
        print "Stop"
        for x in range(5):
            time.sleep(0.1)
            stop()

    #named after method fwd() in GoPiGo lib
    def fwd(self):
        self.status['ismoving'] = True
        print "Fwd"
        for x in range(10):
            time.sleep(0.1)
            fwd()

    #used to tell the main loop to keep going unless something goes wrong
    def keepGoing(self):
        if self.status['dist'] < STOP_DISTANCE:
            print "WARNING 03: Too close to object"
            return False
            ###########
            ###Bobby- This is my change to fix your volt
            ###########
        elif volt() > 14 or volt() < 6: #check voltage and turn off robot is voltage is under 6V or above 14V
            print VOLT
            return False
            ###########
            ###Bobby- This is my change to fix your volt
            ###########
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
        #dancer = threading.Thread(target=servoShake, args=(self))
        #dancer.start()
        self.servoShake()
        self.checkDistance()
        self.backNForth()
        self.checkDistance()
        self.strobe()
        self.checkDistance()
        self.servoShake()
        self.checkDistance()
        #dancer.join()

    def spin(self):
        for x in range(5):
            time.sleep(0.1)
            set_speed(251)
            left_rot()

    def backNForth(self):
        for x in range(5):
            time.sleep(0.1)
            set_speed(251)
            fwd()
            time.sleep(2)
            bwd()
            time.sleep(2)

    def strobe(self):
        print "let's have a rager!"
        for x in range(7):
            led_on(1)
            time.sleep(.3)
            led_off(0)
            time.sleep(.3)
            led_off(1)
            time.sleep(.3)
            led_on(0)
            time.sleep(.3)

    def servoShake(self):
        for x in range(10):
            servo(120)
            time.sleep(.5)
            servo(30)

    def servoSweep(self):
        for ang in range(20, 160, 5):
            if ang % 3 == 0:
                servo(ang)
                time.sleep(.1)
######
###### MAIN APP STARTS HERE
######
pinkie = Pigo()

while pinkie.keepGoing():
    pinkie.checkDistance()
    #pinkie.fwd()
    #time.sleep(.1)
    #pinkie.stop()
    #pinkie.checkDistance()
    pinkie.dance()

pinkie.stop()
del pinkie
