# Return oof sound effect
This program returns the old & iconic "oof" sound effect to your roblox installation.
The program is set to automatically run on startup so that when roblox updates, the program (eventually) takes care of replacing the new `ouch.ogg` sound with the old one *(again)*.

I mostly made this program to learn how git works, but the trigger point was that when you get damaged in Critical Strike, you hear the new sound effect and I can't stand hearing sneeze noises every single time when I get damaged lol.
## Downloads

Head over to the [releases page](https://github.com/OctaNebula/return-oof-sound/releases/tag/release) to download the installer for the program.

The program also requires python to be installed on your system, you can download it [here](https://www.python.org/downloads/).

It may or may not get flagged by windows defender (I genuinely have no idea why), but it's a false positive, you can check the [virus total scan](https://www.virustotal.com/gui/file/fd4faaac8b3aa1bef99b6cd9b436535f49ca4f7a089fd06a72f937dd96d1212b?nocache=1) if you don't believe me.

## Self building & Manual installation

I personally wouldn't bother self building it because I don't think it's worth the effort, but if you really want to, here's how you can do it:

As with any other python program, you can build the `installer-noexe.py` *(you can also use `installer.py` but that makes the program use the exe file, which kinda ruins the whole point of self-building it in the first place)* file into an executable using [pyinstaller](https://www.pyinstaller.org/).

````bash
pyinstaller --onefile --noconsole installer.py
````

The executable will be located in the `dist` folder.


You can also run it through VSCode with administrator privileges (otherwise it won't work).

Alternatively, you can manually install the program by shoving the `main.py` file into the `C:\Program Files (x86)\ReturnOof\` directory and creating a shortcut to it in the startup folder (`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\`). Don't forget to also put the `ouch.ogg` file in the `C:\Program Files (x86)\ReturnOof\` directory.

## FAQ

> bro what is this a virus 💀💀💀

no you can literally check the source code
for some reason it (sometimes) gets flagged by windows defender but its a false positive dont worry
Also check out the [virus total scan](https://www.virustotal.com/gui/file/fd4faaac8b3aa1bef99b6cd9b436535f49ca4f7a089fd06a72f937dd96d1212b?nocache=1).
If you are THAT scared i'd slip a malicious piece of code in the executable, you are free to build it yourself.

> program does not work!!11!11!1

It might be a bug, and this was a random project I made out of pure boredom to learn how git works so don't really expect me to fix it unless it affects me as well lol.
> I want to contribute to the project and improve your shitty code

I yet have to figure out how GitHub works (no pull request mumbo jumbo for now 😭😭) so for now just send me the modified code on discord (OctaNebula#7531).

> bruh how do i get rid of this thing

To uninstall the program just delete the program directory (C:\Program Files (x86)\ReturnOof\).
Optionally you can also delete the shortcut in the startup folder (C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\).

I could in theory make an uninstaller but I don't really see the point of it when it's just a single directory.