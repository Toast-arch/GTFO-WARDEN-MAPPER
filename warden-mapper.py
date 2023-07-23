### ID LOCATOR R2C2 VERSION 1.1 ##
####      MADE BY ARCHI       ####

import os
import sys
import json

from assets.dataclasses import ID_, ZONE_, ARG_, RESULT_

#PATH TO YOUR GTFO APPDATA FORLDER
directory = "C:/Users/" + os.environ.get("USERNAME") + "/AppData/LocalLow/10 Chambers Collective/GTFO/"

netstatus_files = []

#FINDING LATEST NETSTATUS IN GTFO DIRECTORY
for i in os.listdir(directory):
    if os.path.isfile(os.path.join(directory,i)) and 'NICKNAME_NETSTATUS' in i:
        netstatus_files.append(i)

level_name = ""

#FINDING LEVEL
for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "SelectActiveExpedition :" in line:
        line = line[30:]
        words = line.split()

        rundown_local_index = int(words[4][6:])

        if rundown_local_index == 31:
            level_name += "R7"
        elif rundown_local_index == 32:
            level_name += "R1"
        elif rundown_local_index == 33:
            level_name += "R2"
        elif rundown_local_index == 34:
            level_name += "R3"

        level_tier = words[5][4]
        level_name += level_tier

        level_number = int(words[6]) + 1
        level_name += str(level_number)
        break

arg_list = []
i = 0

while i < len(sys.argv):
    if sys.argv[i][0] == '-':
        new_key = sys.argv[i]
        new_sub_list = []
        i += 1
        while i < len(sys.argv) and sys.argv[i][0] != '-':
            new_sub_list.append(sys.argv[i])
            i += 1
        arg_list.append(ARG_(key=new_key, sub_list=new_sub_list))
    else:
        arg_list.append(ARG_(key=sys.argv[i]))
        i += 1

package_name = level_name
nofile = not os.path.exists("packages/" + package_name + '/' + package_name + ".json")
nomap = False
learning = False
learning_input = False

#ARGUMENT APPLY
for arg in arg_list:
    if arg.key_ == '--help':
        print("usage: warden-mapper.py <package name> [--help] [--nofile] [--nomap] [-l | -L]")
        print()
        print("   nomap\tDo not create map images.")
        print("   l\t\tLook for seed in seed learning data.")
        print("   L\t\tAdvanced seed learning option. Will prompt for data to be mapped to sessionseed.")
        exit()
    if arg.key_ == '--nomap' or nofile:
        nomap = True
    if arg.key_ == '-L':
        learning_input = True
    if arg.key_ == '-l' or learning_input:
        learning = True

#PACKAGE JSON FILE
if not nofile:
    try:
        json_file = open("packages/" + package_name + '/' + package_name + ".json", 'r+')
        json_data = json.load(json_file)
    except IOError:
        print("No file found for " + package_name)
        exit()

#LOADING JSON DATA
zone_list = []
listOfLines = []

seedList = []

keyriList = []
keynameList = []
keyZoneList = []

cargozoneList = []

wardenitem_name_list = []
wardenitem_id_list = []
wardenitem_zone_list = []
wardenitem_areacode_list = []

wardenitem_id_dict = {}


populate_area_mapping_dict = {}
SessionSeed = None

look_for_pickup = nofile or json_data['look for pickup']
look_for_key = nofile or json_data['look for key']
look_for_ids = nofile or json_data['look for IDs']
validate_run = False
validate_run_value = 0

if not nofile:
    validate_run = json_data['validate run']
    validate_run_value = json_data['validate run requirement']

if not nofile:
    for zone in json_data['zones']:
        iddict = {}
        #Loading all IDs
        for id in zone['data']:
            iddict[id['index']] = ID_(index=id['index'], seed=id['seed'], area=id['area'], x=id['x'], y=id['y'], z=id['z'], lock=id['lock'], islocker=id['islocker'], zone_size_preset=zone['size preset'])
                
        #Creating ID List for a zone
        zone_list.append(ZONE_(name=zone['name'], type=zone['type'], iddict=iddict, image_file=zone['map file'], package_name=package_name))

#FINDING LAST RUN LOG
for line in reversed(open(directory + netstatus_files[len(netstatus_files) - 1], 'r', encoding='utf-8').readlines()):
    if "SetBuildSeed, forcedSeed" in line:
        break
    listOfLines.append(line)

#ENUMERATING CARGOS, KEYS, AND IDS
wardenitemID = 0

for index, value in enumerate(listOfLines):
        
    lineToBeRead = value

    #SESSION SEED
    if lineToBeRead[46:55] == "GENERATE!" and learning:
        lineToBeRead = lineToBeRead[46:]

        individualWords = lineToBeRead.split()
        SessionSeed = individualWords[2][:-8]
    #WARDEN ITEM ID
    elif (lineToBeRead[30:89] == "LG_Distribute_WardenObjective.DistributeGatherRetrieveItems" and look_for_pickup):
        lineToBeRead = lineToBeRead[30:]

        individualWords = lineToBeRead.split()
        wardenitemID = int(individualWords[6])

        wardenitem_id_list.append(wardenitemID)
    #HSU NAME
    elif (lineToBeRead[38:72] == "RegisterObjectiveItemForCollection" and look_for_pickup):
        lineToBeRead = lineToBeRead[38:]

        individualWords = lineToBeRead.split()
        if len(individualWords) > 3:
            wardenitem_name_list.append(individualWords[3])
        else:
            wardenitem_name_list.append("")
    #HSU ZONE
    elif (lineToBeRead[151:169] == "HSU_FindTakeSample" and look_for_pickup):
        lineToBeRead = lineToBeRead[151:]
    
        individualWords = lineToBeRead.split()
        wardenitem_zone_list.append("ZONE " + individualWords[3][:-1])
        wardenitem_areacode_list.append(individualWords[5])
    elif (lineToBeRead[18:33] == "LG_PopulateZone" and look_for_pickup):
        lineToBeRead = lineToBeRead[18:]
        
        individualWords = lineToBeRead.split()

        if individualWords[4][26:-1].replace('_', ' ') not in populate_area_mapping_dict:
            populate_area_mapping_dict[individualWords[4][26:-1].replace('_', ' ')] = {}
        populate_area_mapping_dict[individualWords[4][26:-1].replace('_', ' ')][individualWords[2]] = ""
    #WARDEN ITEMS
    elif (lineToBeRead[30:102] == "LG_Distribute_WardenObjective.SelectZoneFromPlacementAndKeepTrackOnCount") and look_for_pickup:
        lineToBeRead = lineToBeRead[30:173]
        
        individualWords = lineToBeRead.split()
        cargozoneList.append(individualWords[5])
        
        if wardenitemID != 128 and wardenitemID != 129 and wardenitemID != 169:
            wardenitem_zone_list.append(individualWords[5][:4] + ' ' + individualWords[5][4:])
    #KEY NAME AND ZONE
    elif (lineToBeRead[35:56] == "CalcAreaWeights START"):
        lineToBeRead = lineToBeRead[35:]

        individualWords = lineToBeRead.split()

        keynameList.append(individualWords[4])
        keyZone = (individualWords[11][:4] + ' ' + individualWords[11][4:])[:-1]
        keyZoneList.append(keyZone)

        if "TryGetZoneFunctionDistribution returning FALSE!!" in listOfLines[index - 2]:
            keyriList.append("0")
    #KEY RI
    elif (lineToBeRead[30:81] == "TryGetExistingGenericFunctionDistributionForSession"):
        lineToBeRead = lineToBeRead[30:186]

        individualWords = lineToBeRead.split()
        keyriList.append(individualWords[12])
    #SEED
    elif (lineToBeRead[15:60] == "GenericSmallPickupItem_Core.SetupFromLevelgen"):
        lineToBeRead = lineToBeRead[15:85]
            
        individualWords = lineToBeRead.split()
        seedList.append(int(individualWords[2][0:10]))

#GENERATING RESULTS
result_zones_dict = {}
wardenitem_name_list.reverse()
wardenitem_zone_list.sort()    

#NOFILE KEYS
for i in range(len(keyZoneList)):
    if keyZoneList[i] not in result_zones_dict:
        result_zones_dict[keyZoneList[i]] = {}
    result_zones_dict[keyZoneList[i]][keynameList[i]] = RESULT_(keynameList[i], "UNK", keyriList[i])

#PURGING WRONG DATA ! SAFE MEASURE !
if len(wardenitem_name_list) != len(wardenitem_zone_list):
    wardenitem_zone_list.clear()
    wardenitem_name_list.clear()

#EXPERIMENTAL POPULATE AREAS
for populate_zone_key in populate_area_mapping_dict:
    populate_area_mapping_dict[populate_zone_key] = dict(reversed(list(populate_area_mapping_dict[populate_zone_key].items())))

    tmp_area = 'A'
    for area_key in populate_area_mapping_dict[populate_zone_key]:
        populate_area_mapping_dict[populate_zone_key][area_key] = tmp_area
        tmp_area = chr(ord(tmp_area) + 1)

#NOFILE HSU
for i in range(len(wardenitem_zone_list)):
    if wardenitem_zone_list[i] not in result_zones_dict:
        result_zones_dict[wardenitem_zone_list[i]] = {}
    if len(wardenitem_areacode_list) != 0:
        result_zones_dict[wardenitem_zone_list[i]][wardenitem_name_list[i]] = RESULT_(wardenitem_name_list[i], populate_area_mapping_dict[wardenitem_zone_list[i]][wardenitem_areacode_list[i]])
    else:
        result_zones_dict[wardenitem_zone_list[i]][wardenitem_name_list[i]] = RESULT_(wardenitem_name_list[i])
        

#MAPPED DATA
if not nofile:
    #MAPPED KEYS
    if json_data['look for key']:
        for key_log_index in range(len(keyZoneList)):
            for zone in zone_list:
                if keyZoneList[key_log_index] == zone.name_:
                    result_zones_dict[zone.name_][keynameList[key_log_index]] = RESULT_(keynameList[key_log_index], zone.iddict_[int(keyriList[key_log_index])].area_, zone.iddict_[int(keyriList[key_log_index])].index_)
                    zone.iddict_[int(keyriList[key_log_index])].draw_container(zone.image_save_, True)

    #MAPPED IDS
    if json_data['look for IDs']:
        valid_item_count = 0
        for zone in zone_list:
            for seed_log in seedList:
                for id_index in zone.iddict_:
                    if seed_log == zone.iddict_[id_index].seed_:
                        valid_item_count += 1
                        if zone.name_ not in result_zones_dict:
                            result_zones_dict[zone.name_] = {}
                        
                        if zone.type_ + "{:0>2d}".format(zone.iddict_[id_index].index_) in result_zones_dict[zone.name_]:
                            result_zones_dict[zone.name_][zone.type_ + "{:0>2d}".format(zone.iddict_[id_index].index_)] = RESULT_(zone.type_, zone.iddict_[id_index].area_, zone.iddict_[id_index].index_, result_zones_dict[zone.name_][zone.type_ + "{:0>2d}".format(zone.iddict_[id_index].index_)].n_ + 1)
                        else:
                            result_zones_dict[zone.name_][zone.type_ + "{:0>2d}".format(zone.iddict_[id_index].index_)] = RESULT_(zone.type_, zone.iddict_[id_index].area_, zone.iddict_[id_index].index_)

                        zone.iddict_[id_index].draw_container(zone.image_save_)

#PRINTING RESULTS IN ORDER
sorted_zones_dict = sorted(result_zones_dict.keys(), key=lambda x:x.lower())

for result_zone_key in sorted_zones_dict:
    print('\033[95m' + result_zone_key + ':' + '\033[0m')

    sorted_results_dict = sorted(result_zones_dict[result_zone_key].keys(), key=lambda x:x.lower())

    for result_key in sorted_results_dict:
        result_zones_dict[result_zone_key][result_key].print_data()

if validate_run:
            if valid_item_count >= validate_run_value:
                print('\033[92m' + "VALID RUN - VALID ITEMS FOUND : " + str(valid_item_count) + '\033[0m')
            else:
                print('\033[91m' + "INVALID RUN - VALID ITEMS FOUND : " + str(valid_item_count) + '\033[0m')

#SAVE ALL IMAGES
if not nomap:
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
    if learning_input:
        print('\033[93m' + "Learning seed: " + SessionSeed + '\033[0m')
        for cargozone in cargozoneList:
            learn_input = input("Cargo " + cargozone + ": ")
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