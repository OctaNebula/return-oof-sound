import os
import urllib.request as urllib2
import winshell
import tkinter as tk

#installs winshell

os.system("pip install winshell")

#asks for admin privileges

os.system("powershell -Command \"Start-Process 'python' -ArgumentList 'installer.py' -Verb RunAs\"")

#creates directory in c:\Program Files (x86)\ReturnOof

os.mkdir("C:\Program Files (x86)\ReturnOof")

#downloads main.py to c:\Program Files (x86)\ReturnOof from github

urllib2.urlretrieve("https://raw.githubusercontent.com/OctaNebula/return-oof-sound/main/main.pyw", "C:\Program Files (x86)\ReturnOof\main.pyw")

#literally the same but for the sound file

urllib2.urlretrieve("https://github.com/OctaNebula/return-oof-sound/raw/main/ouch.ogg", "C:\Program Files (x86)\ReturnOof\ouch.ogg")

#creates a shortcut to the main.py file in the startup folder

winshell.CreateShortcut(Path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\ReturnOof.lnk", Target="C:\Program Files (x86)\ReturnOof\main.pyw")

#creates a popup window to tell the user that the program has been installed

#runs the main.py file

os.system("C:\Program Files (x86)\ReturnOof\main.pyw")

root = tk.Tk()
root.title("Return Oof Sound")
root.geometry("300x100")
root.resizable(False, False)
label = tk.Label(root, text="Return Oof Sound has been installed!")
label.pack()
root.mainloop()
