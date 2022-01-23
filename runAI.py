import sys
import os
exec(str(sys.argv[1]))
imageCount = len(os.listdir("/home/reese/Minnehack_2022/minnehack22/website/images"))
os.rename("current.png", "images/" + str(imageCount+1) + ".png")