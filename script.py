### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

## PIL SETTINGS
background_114 = Image.open("assets/ZONE_114.png")
background_115 = Image.open("assets/ZONE_115.png")
background_118 = Image.open("assets/ZONE_118.png")
background_119 = Image.open("assets/ZONE_119.png")
locker_png = Image.open("assets/locker.png")
box_png = Image.open("assets/box.png")

##PATH TO YOUR GTFO APPDATA FORLDER
directory = "C:/Users/bapti/AppData/LocalLow/10 Chambers Collective/GTFO/"

#JSON DATA BASE
json_file = open("assets/R2C2_Mapping.json")
json_data = json.load(json_file)

##CLASSES
class ID_:
    def __init__(self, index, seed, area, x, y, islocker):
        self.index = index
        self.seed = seed
        self.area = area
        self.x = x
        self.y = y
        self.islocker = islocker

    def print_data(self):
        print("Box Index: {} -> {}".format(self.index, self.area))

    def paste_icon(self, background):
        offset_x = 15
        offset_y = 60
        if self.index < 10:
            offset_x = -8
        if self.islocker:
            background.paste(locker_png, (self.x, self.y), locker_png)
        else:
            background.paste(box_png, (self.x, self.y), box_png)
            offset_y = 20
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/OpenSans-Bold.ttf", 64)
        draw.text((self.x - offset_x, self.y + offset_y),str(self.index),(255,0,0),font=font)
    
    def tojson(self):
        return json.dumps(self.__dict__, indent=4)


#LOADING ZONE 114 IDS
ID_List_114 = []

for id in json_data['data']['zone 114']:
    ID_List_114.append(ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], islocker=id['islocker']))

#LOADING ZONE 115 IDS
ID_List_115 = []

for id in json_data['data']['zone 115']:
    ID_List_115.append(ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], islocker=id['islocker']))

#LOADING ZONE 118 IDS
ID_List_118 = []

for id in json_data['data']['zone 118']:
    ID_List_118.append(ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], islocker=id['islocker']))

#LOADING ZONE 119 IDS
ID_List_119 = []

for id in json_data['data']['zone 119']:
    ID_List_119.append(ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], islocker=id['islocker']))

listOfLines = []
seedList = []
netstatus_files = []

#FINDING LATEST NETSTATUS IN GTFO DIRECTORY
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)) and 'NICKNAME_NETSTATUS' in i:
        netstatus_files.append(i)

#FINDING LAST RUN LOG
for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "CreateKeyItemDistribution" in line:
        break
    listOfLines.append(line)

key_id = 0

#ENUMERATING IDS AND KEYS
for index, value in enumerate(listOfLines):
        
    lineToBeRead = value
    if (lineToBeRead[30:81] == "TryGetExistingGenericFunctionDistributionForSession"):
        lineToBeRead = lineToBeRead[30:186]

        individualWords = lineToBeRead.split()
        key_id = individualWords[12]
    if (lineToBeRead[15:60] == "GenericSmallPickupItem_Core.SetupFromLevelgen"):
        lineToBeRead = lineToBeRead[15:85]
            
        individualWords = lineToBeRead.split()
        seedList.append(individualWords[2][0:10])

#CHECKING AND GENERATING 115 KEY MAP
print("KEY ZONE 115:")
ID_List_115[int(key_id)].print_data()
ID_List_115[int(key_id)].paste_icon(background_115)

valid_id_count = 0

#CHECKING AND GENERATING 114
print("IDS ZONE 114:")
for id_game in seedList:
    for id_check_114 in ID_List_114:
        if id_game == str(id_check_114.seed):
            valid_id_count += 1
            id_check_114.print_data()
            id_check_114.paste_icon(background_114)

#CHECKING AND GENERATING 118
print("IDS ZONE 118:")
for id_game in seedList:
    for id_check_118 in ID_List_118:
        if id_game == str(id_check_118.seed):
            valid_id_count += 1
            id_check_118.print_data()
            id_check_118.paste_icon(background_118)

#CHECKING AND GENERATING 119
print("IDS ZONE 119:")
for id_game in seedList:
    for id_check_119 in ID_List_119:
        if id_game == str(id_check_119.seed):
            valid_id_count += 1
            id_check_119.print_data()
            id_check_119.paste_icon(background_119)

if valid_id_count >= 7:
    print('\033[92m' + "VALID RUN - VALID IDs FOUND : " + str(valid_id_count) + '\033[0m')
else:
    print('\033[91m' + "INVALID RUN - VALID IDs FOUND : " + str(valid_id_count) + '\033[0m')

background_114.save("ZONE_114_GENERATED.png")
background_115.save("ZONE_115_GENERATED.png")
background_118.save("ZONE_118_GENERATED.png")
background_119.save("ZONE_119_GENERATED.png")