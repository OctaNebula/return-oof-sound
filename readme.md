# Return oof sound effect
This program returns the old & iconic "oof" sound effect to your roblox installation.
The program is set to automatically run on startup so that when roblox updates, the program (eventually) takes care of replacing the new `ouch.ogg` sound with the old one *(again)*.

## Downloads

Head over to the [releases page](https://github.com/OctaNebula/return-oof-sound/releases/tag/release) to download the latest version of the program.

The program also requires python to be installed on your system, you can download it [here](https://www.python.org/downloads/).

## Self building & Manual installation

I personally wouldn't bother self building it because i don't think it's worth the effort, but if you really want to, here's how you can do it:

As with any other python program, you can build the `installer.py` file into an executable using [pyinstaller](https://www.pyinstaller.org/).
You can also run it through VSCode with administrator privileges (otherwise it won't work).

````bash
pyinstaller --onefile --noconsole installer.py
````
The executable will be located in the `dist` folder.

Alternatively, you can manually install the program by shoving the `main.py` file into the `C:\Program Files (x86)\ReturnOof\` directory and creating a shortcut to it in the startup folder (`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\`). Don't forget to also put the `ouch.ogg` file in the `C:\Program Files (x86)\ReturnOof\` directory.

## FAQ

> bro what is this a virus 💀💀💀

no you can literally check the source code
for some reason it (sometimes) gets flagged by windows defender but its a false positive dont worry
Also check out the [virus total scan](https://www.virustotal.com/gui/file/2906384b4ffd1ec7e1f2e6b6e0a923f932199e123f267218b75c60f4cf88df85/detection).
If you are THAT scared i'd slip a malicious piece of code in the executable, you are free to build it yourself.

> program does not work!!11!11!1

run the program as administrator, i even said it in the readme smh

other than that it might be a bug, and this was a random project I made out of pure boredom to learn how git works so don't really expect me to fix it lol
> I want to contribute to the project and improve your shitty code

I yet have to figure out how GitHub works (no pull request mumbo jumbo for now 😭😭) so for now just send me the modified code on discord (OctaNebula#7531)

> bruh how do i get rid of this thing

To uninstall the program just delete the program directory (C:\Program Files (x86)\ReturnOof\).
