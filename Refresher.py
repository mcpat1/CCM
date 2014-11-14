#Python is weird!
import subprocess as sub
from time import sleep

#Variables
restTime = 15

#Loop
while True:
    sub.call(["midori","-e","Reload"])
    print "Refresh!"
    sleep(restTime)
