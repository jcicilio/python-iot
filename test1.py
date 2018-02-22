import sched
import time
from random import randint
from datetime import datetime

s1 = '16:54:00'
s2 = '16:56:00'
FMT = '%H:%M:%S'

# set rollover time
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
diff = tdelta.seconds
rollover = (24*360)-diff
scheduler = sched.scheduler(time.time, time.sleep)

def Now():
    return time.strftime(FMT, time.localtime())


def print_event():
    print Now(), s1, s2
    doSchedule()

def getRand():
    return randint(1, 5)

def doSchedule():
    # if at end of schedule for day
    r = getRand()
    if (Now()>s2):
        print Now(), s2
        print "Rolling Over"
        r = rollover

    scheduler.enter(r, 1, print_event, ())


if __name__== "__main__":
    # wait for start time to pass before beginning
    while (Now()<s1):
        print "Waiting to start"
        time.sleep(60)

    print "starting"
    doSchedule()
    scheduler.run()