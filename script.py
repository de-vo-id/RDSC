#[
# Roblox Death Sound Changer
# Creator: DEVOID
# Last update: August 25 2022
#]

##===========================================================================================##
## Import libraries

import urllib.request
import shutil
import json
import os
import platform
from os import path

##===========================================================================================##
## Platform checking

Platform = ""
if platform.system() == "Windows":
    Platform = "Windows"
elif platform.system() == "Darwin":
    Platform = "Mac"
else:
    Platform = "Unsupported"
    print('You are running this script on an unsupported OS: '+str(platform.system()))
    exit()

##===========================================================================================##
## Fetch versions from APIs (Windows only)

LiveRequest = urllib.request.urlopen('https://clientsettings.roblox.com/v2/client-version/WindowsPlayer').read()
BetaRequest = urllib.request.urlopen('https://clientsettings.roblox.com/v2/client-version/WindowsPlayer/channel/zfeatureqt5.15').read()
LiveVersion = json.loads(LiveRequest)
BetaVersion = json.loads(BetaRequest)
if Platform == "Windows":
    if LiveRequest and not BetaRequest:
        os.system('cls' if os.name=='nt' else 'clear')
        print('Cannot fetch znext version. Skipping.')
    elif not LiveRequest:
        os.system('cls' if os.name=='nt' else 'clear')
        print('Cannot contact Roblox API to fetch live version.')
        exit()

##===========================================================================================##
## Copy the sound file

if Platform == "Windows":
    LiveLocation = path.expandvars('C:/Users/'+os.path.split(os.path.expanduser('~'))[-1]+'/AppData/Local/'+'Roblox/Versions/'+LiveVersion['clientVersionUpload']+r'/content/sounds')
    BetaLocation = path.expandvars('C:/Users/'+os.path.split(os.path.expanduser('~'))[-1]+'/AppData/Local/'+'Roblox/Versions/'+BetaVersion['clientVersionUpload']+r'/content/sounds')

    if os.path.isdir(LiveLocation) == False and os.path.isdir(BetaLocation) == False:
        os.system('cls' if os.name=='nt' else 'clear')
        print('Roblox directory not found. Is Roblox installed?')
        exit()
    if os.path.isdir(LiveLocation) == True: 
        File = os.path.abspath("ouch.ogg")
        shutil.copy2(File, LiveLocation)
        os.system('cls' if os.name=='nt' else 'clear')
        print('Found live client and copied sound file.')
    if os.path.isdir(BetaLocation) == True: 
        File = os.path.abspath("ouch.ogg")
        shutil.copy2(File, BetaLocation)
        os.system('cls' if os.name=='nt' else 'clear')
        print('Found beta client and copied sound file.')
    print('Enjoy!')
    input("Press Enter to continue...")
elif Platform == "Mac":
    Location = path.expandvars('/Applications/Roblox.app/Contents/Resources/content/sounds')   
    if os.path.isdir(Location) == False: 
        os.system('cls' if os.name=='nt' else 'clear')
        print('Roblox directory not found. Is Roblox installed?')
        exit()
    File = os.path.abspath("ouch.ogg")
    shutil.copy2(File, Location)
    print('Found client and copied sound file. Enjoy!')
