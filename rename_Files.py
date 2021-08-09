import os
from datetime import datetime

path = 'D:\\Media\\Sony\\vlog\\unsorted'
files = os.listdir(path)

for f in files:
    oldName = path + '\\' + f

    timeMod = os.path.getmtime(oldName)
    timeString = datetime.utcfromtimestamp(timeMod).strftime('%Y-%m-%d_%H-%M-%S')

    newName = path + '\\' + timeString + '.mp4'
    print(newName)

    os.rename(oldName, newName)