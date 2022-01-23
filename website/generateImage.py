
from password_strength import PasswordStats
from pass_checkerf import passStrength
import re
import sys
import os
import random
import csv
import subprocess
import time
import math
password = str(sys.argv[1])
filename = str(sys.argv[2])

strengthScore = passStrength(password, PasswordStats)

file = open('score.txt', 'w')
file.write(str(strengthScore))
file.close()

classes = []
with open('/home/reese/Minnehack_2022/minnehack22/classes.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
      classes.append(row[1])

def getKey():
    key = random.randint(0, len(classes))
    return classes[key]

def getCompKey():
    words = ["fractal", "spiral", "pattern", "network", "geometric", "chaos"]
    key = random.randint(0, 5)
    return words[key]
os.system("echo " + str(strengthScore) + "#")
cmdString = ""
cmdString = ("cgd --device cuda --image_size 256 --prompts \"" + password + ":1")
complexityWeight = 0.0025*strengthScore
prompts = 1 + int(abs(strengthScore)/ 40)
for i in range(0, prompts):
    cmdString += ("|" + getKey() + ":" + str(complexityWeight)) 
if(strengthScore > 50):
    cmdString += ("|" + getCompKey() + ":" + str(4*complexityWeight)) 
    cmdString += "\""
    cmdString += " --clip_guidance_scale 2000 -respace 150"
else:
    cmdString += "\""
    cmdString+= " -respace 25"
# os.system("echo CMD STRING: " + cmdString)
os.system("exec " + cmdString)

os.rename("current.png", "/home/reese/Minnehack_2022/minnehack22/website/images/" + filename + ".png")