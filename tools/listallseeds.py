### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
import sys
import json

#PATH TO YOUR GTFO APPDATA FORLDER
directory = "C:/Users/"+os.environ.get("USERNAME")+"/AppData/LocalLow/10 Chambers Collective/GTFO/"

listOfLines = []
seedList = []
keyList = []
netstatus_files = []

#FINDING LATEST NETSTATUS IN GTFO DIRECTORY
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)) and 'NICKNAME_NETSTATUS' in i:
        netstatus_files.append(i)

#FINDING LAST RUN LOG
for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "Artifacts" in line:
        break
    listOfLines.append(line)

#ENUMERATING IDS AND KEYS
for index, value in enumerate(listOfLines):
        
    lineToBeRead = value
    if (lineToBeRead[30:81] == "TryGetExistingGenericFunctionDistributionForSession"):
        lineToBeRead = lineToBeRead[30:186]

        individualWords = lineToBeRead.split()
        keyList.append(individualWords[12])
    if (lineToBeRead[15:60] == "GenericSmallPickupItem_Core.SetupFromLevelgen"):
        lineToBeRead = lineToBeRead[15:85]
            
        individualWords = lineToBeRead.split()
        seedList.append(individualWords[2][0:10])

found_seeds_list = [
    1344295424,
    1433722496,
    882867584,
    1248821120,
    254974336,
    1609558400,
    200506560,
    939493248,
    2059003520,
    1039172736,
    1199609856,
    130123320,
    340871392,
    166939088,

    1934982400,
    1046386880,
    1771112960,
    433089536,
    434411392,
    1256315008,
    883189120,
    381356064,
    2120752256,

    732516608,
    1243389824,
    599568640,
    1594787456,
    1503030784,
    1671259136,
    71303464,
    2050920576,
    1805682816,

    1847424512,
    528858272,
    704022592,
    467048896,
    1640979968,
    469385184,
]

print("KEYS FOUND : " + str(len(keyList)))
for key in keyList:
    print(key)

print("SEEDS FOUND : " + str(len(seedList)))
print("NEW SEEDS :")
for seed in seedList:
    if seed not in seedList:
        print(seed)