from playsound import playsound
from os import listdir
from random import randint

path = "/temp/sounds/"
soundFiles = listdir(path)

def playSound():
    # https://www.nps.gov/subjects/sound/gallery.htm
    index = randint(0, len(soundFiles)-1)
    playsound(path + soundFiles[index])



if __name__== "__main__":
   playSound()
   playSound()
   playSound()
   playSound()
   playSound()
