### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json

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

"""
#################################
## HARDCODED DATABASE FOR R2C2 ##
#################################

ID_List_114.append(ID_(index=0, seed=902445824, area="A", x=550, y= 620, islocker=False))
ID_List_114.append(ID_(index=1, seed=193228176, area="A", x=70, y= 900, islocker=False))
ID_List_114.append(ID_(index=2, seed=1392375680, area="A", x=50, y= 600, islocker=True))
ID_List_114.append(ID_(index=3, seed=108037848, area="A", x=50, y= 1200, islocker=True))
ID_List_114.append(ID_(index=4, seed=691456256, area="A", x=540, y= 540, islocker=True))
ID_List_114.append(ID_(index=5, seed=2044321280, area="A", x=400, y= 880, islocker=True))

ID_List_114.append(ID_(index=6, seed=1715163648, area="B", x=1200, y= 1150, islocker=True))
ID_List_114.append(ID_(index=7, seed=1704448256, area="B", x=830, y= 1200, islocker=False))
ID_List_114.append(ID_(index=8, seed=568560896, area="B", x=500, y= 150, islocker=False))
ID_List_114.append(ID_(index=9, seed=263707664, area="B", x=1050, y= 820, islocker=True))
ID_List_114.append(ID_(index=10, seed=1977231744, area="B", x=620, y= 750, islocker=False))
ID_List_114.append(ID_(index=11, seed=1513845248, area="B", x=750, y= 550, islocker=True))
ID_List_114.append(ID_(index=12, seed=1111940352, area="B", x=900, y= 900, islocker=True))
ID_List_114.append(ID_(index=13, seed=132742704, area="B", x=1250, y= 680, islocker=False))
ID_List_114.append(ID_(index=14, seed=1745413376, area="B", x=1070, y= 700, islocker=True))
ID_List_114.append(ID_(index=15, seed=193783648, area="B", x=1180, y= 630, islocker=True))
ID_List_114.append(ID_(index=16, seed=23400414, area="B", x=750, y= 1000, islocker=True))
ID_List_114.append(ID_(index=17, seed=740991680, area="B", x=950, y= 680, islocker=True))
ID_List_114.append(ID_(index=18, seed=1035849152, area="B", x=650, y= 20, islocker=False))
ID_List_114.append(ID_(index=19, seed=1063610624, area="B", x=850, y= 20, islocker=False))

ID_List_114.append(ID_(index=20, seed=1869450880, area="C", x=850, y= 1330, islocker=False))
ID_List_114.append(ID_(index=21, seed=1233898112, area="C", x=1490, y= 1290, islocker=True))
ID_List_114.append(ID_(index=22, seed=2075324672, area="C", x=1150, y= 1310, islocker=True))
ID_List_114.append(ID_(index=23, seed=1079995008, area="C", x=1250, y= 1370, islocker=True))

ID_List_114.append(ID_(index=24, seed=2041384320, area="D", x=1270, y= 370, islocker=True))
ID_List_114.append(ID_(index=25, seed=416855136, area="D", x=1400, y= 300, islocker=True))
ID_List_114.append(ID_(index=26, seed=795424640, area="D", x=1530, y= 650, islocker=True))
ID_List_114.append(ID_(index=27, seed=1719594752, area="D", x=1350, y= 920, islocker=False))
ID_List_114.append(ID_(index=28, seed=1615299840, area="D", x=1200, y= 200, islocker=True))
ID_List_114.append(ID_(index=29, seed=1502357376, area="D", x=1540, y= 900, islocker=False))
ID_List_114.append(ID_(index=30, seed=1214851072, area="D", x=1100, y= 200, islocker=True))
ID_List_114.append(ID_(index=31, seed=662580288, area="D", x=1050, y= 200, islocker=True))
ID_List_114.append(ID_(index=32, seed=837992704, area="D", x=1190, y= 100, islocker=True))

ID_List_119.append(ID_(index=0, seed=4278100, area="A", x=1320, y=1070, islocker=False))
ID_List_119.append(ID_(index=1, seed=1515655808, area="A", x=1200, y=1040, islocker=True))
ID_List_119.append(ID_(index=2, seed=1514311424, area="A", x=1080, y=730, islocker=False))
ID_List_119.append(ID_(index=3, seed=1898678016, area="A", x=1120, y=670, islocker=False))
ID_List_119.append(ID_(index=4, seed=248403728, area="A", x=930, y=990, islocker=True))
ID_List_119.append(ID_(index=5, seed=665892608, area="A", x=1140, y=1020, islocker=True))

ID_List_119.append(ID_(index=6, seed=662422144, area="B", x=1070, y=420, islocker=False))
ID_List_119.append(ID_(index=7, seed=1856521856, area="B", x=1020, y=380, islocker=False))
ID_List_119.append(ID_(index=8, seed=875401600, area="B", x=975, y=270, islocker=True))
ID_List_119.append(ID_(index=9, seed=1585691904, area="B", x=1120, y=270, islocker=False))
ID_List_119.append(ID_(index=10, seed=731438720, area="B", x=560, y=400, islocker=True))
ID_List_119.append(ID_(index=11, seed=1623561856, area="B", x=700, y=10, islocker=True))

ID_List_119.append(ID_(index=12, seed=636640896, area="C", x=260, y=40, islocker=True))
ID_List_119.append(ID_(index=13, seed=154068448, area="C", x=200, y=20, islocker=True))
ID_List_119.append(ID_(index=14, seed=150273632, area="C", x=740, y=600, islocker=True))
ID_List_119.append(ID_(index=15, seed=2124347392, area="C", x=80, y=20, islocker=True))
ID_List_119.append(ID_(index=16, seed=72459192, area="C", x=270, y=280, islocker=True))
ID_List_119.append(ID_(index=17, seed=2104839296, area="C", x=400, y=40, islocker=True))

ID_List_119.append(ID_(index=18, seed=2038409856, area="D", x=350, y=970, islocker=True))
ID_List_119.append(ID_(index=19, seed=244358304, area="D", x=180, y=1000, islocker=True))
ID_List_119.append(ID_(index=20, seed=1522069248, area="D", x=270, y=1150, islocker=False))
ID_List_119.append(ID_(index=21, seed=1912506752, area="D", x=620, y=950, islocker=True))
ID_List_119.append(ID_(index=22, seed=857092480, area="D", x=270, y=1270, islocker=False))
ID_List_119.append(ID_(index=23, seed=973303616, area="D", x=590, y=1220, islocker=True))

#####################
## END OF DATABASE ##
#####################
"""

"""
json_string = json.dumps([ob.__dict__ for ob in ID_List_119], indent=4)
filename = 'R2C2_Zone_119_Mapping.json'

with open(filename, 'w') as file:
    file.write(json_string)

exit()
"""

listOfLines = []
seedList = []
netstatus_files = []

for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)) and 'NICKNAME_NETSTATUS' in i:
        netstatus_files.append(i)

for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "CreateKeyItemDistribution" in line:
        break
    listOfLines.append(line)

if len(listOfLines) == 0:
    print("NO ACTIVE NETSTATUS FILE FOUND AT : {}".format(directory))
    exit()

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