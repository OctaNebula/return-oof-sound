import os
import shutil

#searches for the ouch.ogg file in the directory in C:\Users\%username%\AppData\Local\Roblox\Versions and returns its path
def find_ouch():
    for root, dirs, files in os.walk(os.path.expandvars("%localappdata%\Roblox\Versions")):
        for file in files:
            if file == "ouch.ogg":
                return os.path.join(root, file)

path = find_ouch()

os.remove(path)

originalouch = r'C:\Users\%userprofile%\Documents\ReturnOof\ouch.ogg'
target = path

shutil.copyfile(originalouch, target)
