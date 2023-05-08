originalouch = r'C:\Program Files (x86)\ReturnOof\ouch.ogg'

import os
import shutil

#finds both ouch.ogg files
def find_ouch_1():
    for root, dirs, files in os.walk(os.path.expandvars("%localappdata%\Roblox\Versions")):
        for file in files:
            if len(dirs) == 2:
                del dirs[0]
            if file == "ouch.ogg":
                return os.path.join(root, file)
def find_ouch_2():
    for root, dirs, files in os.walk(os.path.expandvars("%localappdata%\Roblox\Versions")):
        for file in files:
            if len(dirs) == 2:
                del dirs[1]
            if file == "ouch.ogg":
                return os.path.join(root, file)

#replaces both ouch.ogg files
def replace(path):
    os.remove(path)
    shutil.copyfile(originalouch, path)

replace(find_ouch_1())
replace(find_ouch_2())