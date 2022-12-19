### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
import sys
import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#PATH TO YOUR GTFO APPDATA FORLDER
directory = "C:/Users/" + os.environ.get("USERNAME") + "/AppData/LocalLow/10 Chambers Collective/GTFO/"

#ARGUMENT READING
if len(sys.argv) == 1:
    print("Please indicate package (level) name.")
    exit()

arg_list = []
notarg_list = []

for word in sys.argv[1:]:
    if word[0] == '-':
        arg_list.append(word[1:])
    else:
        notarg_list.append(word)

package_name = notarg_list[0]

#JSON DATA BASE
json_file = open(package_name + '/' + package_name + ".json", 'r+')
json_data = json.load(json_file)

## LOADING PIL IMAGE SETTINGS
map_image_list = []

for zone in json_data['zones']:
    map_image_list.append(Image.open(package_name + '/' + zone['map file']))

locker_png = Image.open("assets/locker.png")
box_png = Image.open("assets/box.png")

##CLASSES
class ID_:
    def __init__(self, index, seed, area, x, y, z, lock, islocker):
        self.index_ = index
        self.seed_ = seed
        self.area_ = area
        self.x_ = x
        self.y_ = y
        self.z_ = z
        self.lock_ = lock
        self.islocker_ = islocker

    def print_data(self):
        print("Box Index: {} -> {}".format(self.index_, self.area_))

    def draw_container(self, background):
        offset_x = 15
        offset_y = 60
        if self.index_ < 10:
            offset_x = -8
        if self.islocker_:
            background.paste(locker_png, (self.x_, self.y_), locker_png)
        else:
            background.paste(box_png, (self.x_, self.y_), box_png)
            offset_y = 20
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/OpenSans-Bold.ttf", 55)
        r, g, b = 0, 255, 0
        if self.lock_ == 1:
            r, g, b = 250, 218, 94
        elif self.lock_ == 2:
            r, g, b = 255, 0, 0

        draw.text((self.x_ - offset_x, self.y_ + offset_y),str(self.index_),(r,g,b),font=font)
        if self.z_ > 0:
            draw.text((self.x_ + 10, self.y_ - 20),'^',(0,0,0),font=font)
        elif self.z_ < 0:
            draw.text((self.x_ + 10, self.y_ - 20),'v',(0,0,0),font=font)
    
    def tojson(self):
        return json.dumps(self.__dict__, indent=4)

class ZONE_:
    def __init__(self, name, index, type, idlist, image_file):
        self.name_ = name
        self.index_ = index
        self.type_ = type
        self.idlist_ = idlist
        self.image_file_ = image_file
        self.image_ = Image.open(package_name + '/' + image_file)
    
    def save_image(self):
        self.image_.save(self.image_file_[:len(self.image_file_) - 4] + "_GENERATED.png")

#LOADING JSON DATA
zone_list = []

for zone in json_data['zones']:
    idlist = []
    #Loading all IDs
    for id in zone['data']:
        idlist.append(ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], z=id['z'], lock=id['lock'], islocker=id['islocker']))
    print("Loading " + zone['name'] + " with map file " + zone['map file'])
    
    #Creating ID List for a zone
    zone_list.append(ZONE_(name=zone['name'], index= zone['index'], type=zone['type'], idlist= idlist, image_file=zone['map file']))

listOfLines = []
seedList = []
keyList = []
cargozoneList = []
netstatus_files = []
SessionSeed = None

#FINDING LATEST NETSTATUS IN GTFO DIRECTORY
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)) and 'NICKNAME_NETSTATUS' in i:
        netstatus_files.append(i)

#FINDING LAST RUN LOG
for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "SetBuildSeed, forcedSeed" in line:
        break
    listOfLines.append(line)

#ENUMERATING CARGOS, KEYS, AND IDS
for index, value in enumerate(listOfLines):
        
    lineToBeRead = value
    if (lineToBeRead[46:55] == "GENERATE!" and ('l' in arg_list or 'L' in arg_list)):
        lineToBeRead = lineToBeRead[46:]

        individualWords = lineToBeRead.split()
        SessionSeed = individualWords[2][:-8]
    elif (lineToBeRead[30:102] == "LG_Distribute_WardenObjective.SelectZoneFromPlacementAndKeepTrackOnCount") and json_data['look for cargo']:
        lineToBeRead = lineToBeRead[30:173]
        
        individualWords = lineToBeRead.split()
        cargozoneList.append(individualWords[5])
        print("CARGO FOUND AT " + individualWords[5])
    elif (lineToBeRead[30:81] == "TryGetExistingGenericFunctionDistributionForSession") and json_data['look for key']:
        lineToBeRead = lineToBeRead[30:186]

        individualWords = lineToBeRead.split()
        keyList.append(individualWords[12])
    elif (lineToBeRead[15:60] == "GenericSmallPickupItem_Core.SetupFromLevelgen") and json_data['look for IDs']:
        lineToBeRead = lineToBeRead[15:85]
            
        individualWords = lineToBeRead.split()
        seedList.append(individualWords[2][0:10])

#CHECKING AND GENERATING KEY MAPS
if json_data['look for key']:
    for zone in zone_list:
        if zone.type_ == "KEY":
            for key_log in keyList:
                print("KEY FOUND " + zone.name_ + ':')
                zone.idlist_[int(key_log)].print_data()
                zone.idlist_[int(key_log)].draw_container(zone.image_)

#CHECKING AND GENERATING ID MAPS
if json_data['look for IDs']:
    valid_id_count = 0

    for zone in zone_list:
        if zone.type_ == "ID":
            print("IDS FOUND " + zone.name_ + ':')
            for id_log in seedList:
                for id_check in zone.idlist_:
                    if id_log == str(id_check.seed_):
                        valid_id_count += 1
                        id_check.print_data()
                        id_check.draw_container(zone.image_)

    if valid_id_count >= 7:
        print('\033[92m' + "VALID RUN - VALID IDs FOUND : " + str(valid_id_count) + '\033[0m')
    else:
        print('\033[91m' + "INVALID RUN - VALID IDs FOUND : " + str(valid_id_count) + '\033[0m')

#SAVE ALL IMAGES
for zone in zone_list:
    zone.save_image()

#SEED LEARNING !!! WIP !!!
if SessionSeed:
    learn_input_list = []

    if 'seed learning data' not in json_data:
        json_data['seed learning data'] = []
    else:
        for seed_data in json_data['seed learning data']:
            if str(seed_data['seed']) == SessionSeed:
                print('\033[92m' + "SEED FOUND IN LEARNING DATA: " + SessionSeed + '\033[0m')
                json_formatted_str = json.dumps(seed_data, indent=2)
                print(json_formatted_str)
                exit()

    #HARDCODED FOPR R2A1
    if 'L' in arg_list:
        print('\033[93m' + "Learning seed: " + SessionSeed + '\033[0m')
        for cargozone in cargozoneList:
            print("Cargo " + cargozone + ": ", end='')
            learn_input = input()
            if learn_input == "":
                print("Learning cancelled...")
                exit()
            learn_input_list.append((cargozone, learn_input))
    else:
        exit()

    json_object = {"seed": int(SessionSeed)}

    for learn_input in learn_input_list:
        json_object[learn_input[0]] = learn_input[1]

    json_data['seed learning data'].append(json_object)
    json_file.seek(0)
    json.dump(json_data, json_file, indent=4)