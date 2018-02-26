import sched
import time
from datetime import datetime
from playsound import playsound
from os import listdir
from random import randint


### Setup
# set rollover time
s1 = '12:15:00'
s2 = '12:45:00'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
diff = tdelta.seconds
rollover = (24*60*60)-diff
scheduler = sched.scheduler(time.time, time.sleep)
path = "/temp/sounds/"
soundFiles = listdir(path)

def Now():
    return time.strftime(FMT, time.localtime())

def playSound():
    # https://www.nps.gov/subjects/sound/gallery.htm
    print "playing", Now(), s1, s2
    index = randint(0, len(soundFiles)-1)
    playsound(path + soundFiles[index])

    doSchedule()

def getRand():
    return randint(60, 600)

def doSchedule():
    # if at end of schedule for day
    r = getRand()
    if (Now()>s2):
        print Now(), s2
        print "Rolling Over"
        r = rollover

    print "next sound starting in " + str(r) + " seconds"
    scheduler.enter(r, 1, playSound, ())

if __name__== "__main__":
    # wait for start time to pass before beginning
    while (Now()<s1):
        print "Waiting to start"
        time.sleep(60)

    print "starting"
    doSchedule()
    scheduler.run()