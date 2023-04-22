import os
import urllib.request as urllib2
import winshell
import tkinter as tk

#installs winshell

os.system("pip install winshell")

#creates directory in C:\Users\%username%\Documents\ReturnOof

os.makedirs(r"C:\Users\%username%\Documents\ReturnOof")

#downloads main.py to C:\Users\%username%\Documents\ReturnOof from github

urllib2.urlretrieve("https://raw.githubusercontent.com/OctaNebula/return-oof-sound/main/main.pyw", r"C:\Users\%username%\Documents\ReturnOof\main.pyw")

#literally the same but for the sound file

urllib2.urlretrieve("https://github.com/OctaNebula/return-oof-sound/raw/main/ouch.ogg", r"C:\Users\%username%\Documents\ReturnOof\ouch.ogg")

#creates a shortcut to the main.py file in the startup folder

winshell.CreateShortcut(Path=r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\ReturnOof.lnk", Target=r"C:\Users\%username%\Documents\ReturnOof\main.pyw")

#creates a popup window to tell the user that the program has been installed

#runs the main.py file

os.system(r"C:\Users\%username%\Documents\ReturnOof\main.pyw")

root = tk.Tk()
root.title("Return Oof Sound")
root.geometry("300x100")
root.resizable(False, False)
label = tk.Label(root, text="Return Oof Sound has been installed!")
label.pack()
root.mainloop()
