import sched
import time
from random import randint
from datetime import datetime

s1 = '16:00:00'
s2 = '16:20:00'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
diff = tdelta.seconds
datetime.now()
scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name, start):
    now = time.time()
    elapsed = int(now - start)
    print('EVENT: {} elapsed={} name={}'.format(time.ctime(now), elapsed, name))
    doSchedule()

def getRand():
    return randint(0, 5)

def doSchedule():
    # if at end of schedule for day
    r = getRand()
    scheduler.enter(r, 1, print_event, (r, start))


if __name__== "__main__":
    # wait for start time to pass before beginning
    doSchedule()
    scheduler.run()