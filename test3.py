import sched
import time
from datetime import datetime
from playsound import playsound
from os import listdir
from random import randint

### Setup
# set rollover time
startTime = '12:55:00'
endTime = '13:10:00'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(endTime, FMT) - datetime.strptime(startTime, FMT)
diff = tdelta.seconds
rollover = (24*60*60)-diff
scheduler = sched.scheduler(time.time, time.sleep)
path = "/temp/sounds/"
soundFiles = listdir(path)

def Now():
    return time.strftime(FMT, time.localtime())

def playSound():
    # https://www.nps.gov/subjects/sound/gallery.htm
    index = randint(0, len(soundFiles)-1)
    print "playing", soundFiles[index], Now(), startTime, endTime
    playsound(path + soundFiles[index])

    doSchedule()

def getRand():
    return randint(60, 600)

def doSchedule():
    # if at end of schedule for day
    r = getRand()
    if (Now()>endTime):
        print Now(), endTime
        print "Rolling Over"
        r = rollover

    print "next sound starting in " + str(r) + " seconds"
    scheduler.enter(r, 1, playSound, ())

if __name__== "__main__":
    # wait for start time to pass before beginning
    while (Now()<startTime or Now()>endTime):
        print "Waiting to start at ", startTime
        time.sleep(60)

    print "starting"
    doSchedule()
    scheduler.run()