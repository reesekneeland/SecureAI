
from password_strength import PasswordStats
from minnehack22.website.pass_checkerf import passStrength
import re
import sys
import os
import random
import csv
import subprocess
import time
os.system("echo script running!")
password = str(sys.argv[1])
filename = str(sys.argv[2] + ".png")
out = subprocess.Popen(['screen', '-ls'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
while("AIGen" in str(stdout)): #Run this thread in an infinite loop until there are no open screens
    time.sleep(10)
    out = subprocess.Popen(['screen', '-ls'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print("waiting for other processes to complete")

strengthScore = passStrength(password, PasswordStats)
os.system("echo strengthScore: " + str(strengthScore))
classes = []
with open('/home/reese/Minnehack_2022/minnehack22/classes.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      classes.append(row[1])

def getKey():
    key = random.randint(0, len(classes))
    return classes[key]



cmdString = ""
os.system("echo generating")
cmdString = ("cgd --image_size 256 -respace 150 --prompts \"" + password + ":1")
complexityWeight = 0.005*strengthScore
prompts = 1 + int(strengthScore / 30)
os.system("echo promptCount: " + str(prompts))
for i in range(0, prompts):
    cmdString += ("|" + getKey() + ":" + str(complexityWeight)) 
cmdString += "\""
if(strengthScore > 50):
    cmdString += " --clip_guidance_scale 2000"
os.system("echo CMD STRING: " + cmdString)
os.system("screen -S AIGen " + cmdString)
os.system("echo image creation done")
out = subprocess.Popen(['screen', '-ls'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
print("processing")
while("AIGen" in str(stdout)):
    time.sleep(1)
    out = subprocess.Popen(['screen', '-ls'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    print("processing")

os.rename("current.png", "/home/reese/Minnehack_2022/minnehack22/website/images/" + filename)