import shutil, os
from pathlib import Path
from datetime import datetime

NUMBER_OF_BACKUPS = 10

time = datetime.now()
numOfDirs = 0

World_Location = os.path.expanduser("~/Servers/minecraft/")
Backup_Location = os.path.expanduser("~/Servers/World_Backups/")

current_time = time.strftime("%m-%d-%Y.%H%M%S")
folderName = "1_%s-world" % current_time
current_backup = os.path.join(Backup_Location, folderName)

print(current_time)

for dirs in os.scandir(Backup_Location):
    numOfDirs += 1
    splitName = str(dirs).split('_')
    newNumber = int(splitName[0][len(splitName[0])-1]) + 1
    newDirName = str(newNumber) + "_" + splitName[1][0 : len(splitName[1])-2] 
    os.rename(dirs, Backup_Location + newDirName)    
    
    if newNumber > NUMBER_OF_BACKUPS:
        os.rmdir(os.path.join(Backup_Location, newDirName))

os.mkdir(current_backup)
print("New backup directory created")

try:
    shutil.copytree(os.path.join(World_Location, "world"), os.path.join(current_backup, "world"))
    print("Backed up world")
except Error as err:
    errors.extend(err.args[0])
try:
    shutil.copytree(os.path.join(World_Location, "world_nether"), os.path.join(current_backup, "world_nether"))
    print("Backed up nether")
except Error as err:
    errors.extend(err.args[0])
try:
    shutil.copytree(os.path.join(World_Location, "world_the_end"), os.path.join(current_backup, "world_the_end"))
    print("Backed up end")
except Error as err:
    errors.extend(err.args[0])
print("Backup complete")
