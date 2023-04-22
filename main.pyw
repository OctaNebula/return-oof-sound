import os

#searches for the ouch.ogg file in the directory in C:\Users\%username%\AppData\Local\Roblox\Versions, and replaces it with the ouch.ogg file in the directory of the program
def replace():
    for root, dirs, files in os.walk(os.getenv('LOCALAPPDATA') + r"\Roblox\Versions"):
        for file in files:
            if file == "ouch.ogg":
                os.remove(os.path.join(root, file))
                os.system("copy ouch.ogg " + os.path.join(root, file))

replace()
