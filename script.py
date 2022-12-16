### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

## PIL SETTINGS
background = Image.open("assets/ZONE_114.png")
locker_png = Image.open("assets/locker.png")
box_png = Image.open("assets/box.png")

##PATH TO YOUR GTFO APPDATA FORLDER
directory = "C:/Users/bapti/AppData/LocalLow/10 Chambers Collective/GTFO/"

##CLASSES
class ID_:
    def __init__(self, index, seed, area, firstname, lastname):
        self.index = index
        self.seed = seed
        self.area = area
        self.firstname = firstname
        self.lastname = lastname

    def print_data(self):
        print("Box Index: {}".format(self.index))

class CONTAINER_:
    def __init__(self, index, x, y, islocker):
        self.index = index
        self.x = x
        self.y = y
        self.islocker = islocker

    def paste(self, background):
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

#################################
## HARDCODED DATABASE FOR R2C2 ##
#################################

#ZONE 114 IDS
ID_List_114 = []

ID_List_114.append(ID_(index=0, seed=902445824, area="A", firstname="", lastname=""))
ID_List_114.append(ID_(index=1, seed=193228176, area="A", firstname="", lastname=""))
ID_List_114.append(ID_(index=2, seed=1392375680, area="A", firstname="", lastname=""))
ID_List_114.append(ID_(index=3, seed=108037848, area="A", firstname="", lastname=""))
ID_List_114.append(ID_(index=4, seed=691456256, area="A", firstname="", lastname=""))
ID_List_114.append(ID_(index=5, seed=2044321280, area="A", firstname="", lastname=""))

ID_List_114.append(ID_(index=6, seed=1715163648, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=7, seed=1704448256, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=8, seed=568560896, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=9, seed=263707664, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=10, seed=1977231744, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=11, seed=1513845248, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=12, seed=1111940352, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=13, seed=132742704, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=14, seed=1745413376, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=15, seed=193783648, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=16, seed=23400414, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=17, seed=740991680, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=18, seed=1035849152, area="B", firstname="", lastname=""))
ID_List_114.append(ID_(index=19, seed=1063610624, area="B", firstname="", lastname=""))

ID_List_114.append(ID_(index=20, seed=1869450880, area="C", firstname="", lastname=""))
ID_List_114.append(ID_(index=21, seed=1233898112, area="C", firstname="", lastname=""))
ID_List_114.append(ID_(index=22, seed=2075324672, area="C", firstname="", lastname=""))
ID_List_114.append(ID_(index=23, seed=1079995008, area="C", firstname="", lastname=""))

ID_List_114.append(ID_(index=24, seed=2041384320, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=25, seed=416855136, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=26, seed=795424640, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=27, seed=1719594752, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=28, seed=1615299840, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=29, seed=1502357376, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=30, seed=1214851072, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=31, seed=662580288, area="D", firstname="", lastname=""))
ID_List_114.append(ID_(index=32, seed=837992704, area="D", firstname="", lastname=""))

#ZONE 114 CONTAINERS
CONTAINERS_114_List = []

CONTAINERS_114_List.append(CONTAINER_(index=0, x=550, y= 620, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=1, x=70, y= 900, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=2, x=50, y= 600, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=3, x=50, y= 1200, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=4, x=540, y= 540, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=5, x=400, y= 880, islocker=True))

CONTAINERS_114_List.append(CONTAINER_(index=6, x=1200, y= 1150, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=7, x=830, y= 1200, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=8, x=500, y= 150, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=9, x=1050, y= 820, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=10, x=620, y= 750, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=11, x=750, y= 550, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=12, x=900, y= 900, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=13, x=1250, y= 680, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=14, x=1070, y= 700, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=15, x=1180, y= 630, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=16, x=750, y= 1000, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=17, x=950, y= 680, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=18, x=650, y= 20, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=19, x=850, y= 20, islocker=False))

CONTAINERS_114_List.append(CONTAINER_(index=20, x=850, y= 1330, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=21, x=1490, y= 1290, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=22, x=1150, y= 1310, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=23, x=1250, y= 1370, islocker=True))

CONTAINERS_114_List.append(CONTAINER_(index=24, x=1270, y= 370, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=25, x=1400, y= 300, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=26, x=1530, y= 650, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=27, x=1350, y= 920, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=28, x=1200, y= 200, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=29, x=1540, y= 900, islocker=False))
CONTAINERS_114_List.append(CONTAINER_(index=30, x=1100, y= 200, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=31, x=1050, y= 200, islocker=True))
CONTAINERS_114_List.append(CONTAINER_(index=32, x=1190, y= 100, islocker=True))

#####################
## END OF DATABASE ##
#####################

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
    if (lineToBeRead[15:60] == "GenericSmallPickupItem_Core.SetupFromLevelgen"):
        lineToBeRead = lineToBeRead[15:85]
            
        individualWords = lineToBeRead.split()
        seedList.append(individualWords[2][0:10])

print(seedList)
for id_game in seedList:
    for id_check in ID_List_114:
        if id_game == str(id_check.seed):
            id_check.print_data()
            CONTAINERS_114_List[id_check.index].paste(background)

background.save("ZONE_144_FILLED.png")