import os
from PIL import Image
import json
import sys
import cv2
from assets.dataclasses import ID_, ZONE_, ARG_

def click_event(event, x, y, flags, params):
 
   # checking for left mouse clicks
   if event == cv2.EVENT_LBUTTONDOWN:
      # displaying the coordinates
      # on the Shell
      print(x, ' ', y)
      global global_x
      global_x = x
      global global_y
      global_y = y
      cv2.imshow('window42', cv_img)
      cv2.destroyAllWindows()
      #cv2.destroyWindow('window42')

def open_cv_window():
   cv2.imshow('window42', cv_img)
   cv2.setMouseCallback('window42', click_event)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

if __name__=="__main__":

   package_name = sys.argv[1]

   global global_x
   global_x = -1
   global global_y
   global_y = -1

   json_file = open(os.path.join("packages", package_name, package_name + '.json'), 'r+')

   json_data = json.load(json_file)

   ## LOADING PIL IMAGE ASSETS
   locker_png = Image.open("assets/locker.png")
   box_png = Image.open("assets/box.png")

   name = input("New zone name: ")
   index = int(input("New zone index: "))
   type = input("New zone type: ")
   map_file = input("New zone map file: ")

   json_zone = {
      "name": name,
      "index": index,
      "type": type,
      "map file": map_file,
      "data": []
   }

   number_of_objects = int(input("Number of objects: "))

   for i in range(number_of_objects):
      print("NEW SEEDED CONTAINER: ")

      index = int(input("Object index: "))
      seed = int(input("Object seed: "))
      area = input("Object area: ")

      img_path = os.path.join("packages", package_name, map_file)
      img_path2 = map_file[:-4] + "_preview.png"

      #print("GLOBAL X AND y {} {}".format(global_x, global_y))

      """ cv_img = cv2.imread(img_path, 1)

      cv2.imshow('window42', cv_img)
      cv2.setMouseCallback('window42', click_event)
      cv2.waitKey(0)
      cv2.destroyAllWindows() """
      
      cv_img = cv2.imread(img_path, 1)

      open_cv_window()

      #print("GLOBAL X AND y {} {}".format(global_x, global_y))
   
      id = ID_(x=global_x, y=global_y)
      background = Image.open(img_path)
   
      id.draw_container(background=background, locker_png=locker_png, box_png=box_png)

      background.save(map_file[:-4] + "_preview.png")

      z = int(input("Object z: "))
      lock = int(input("Object lock: "))
      tmp = input("Object islocker: ")
      islocker = tmp == "true" or tmp == "True" or tmp == "1"

      json_id = {
         "index": index,
         "seed": seed,
         "area": area,
         "x": global_x,
         "y": global_y,
         "z": z,
         "lock": lock,
         "islocker": islocker
      }

      json_zone['data'].append(json_id)
      json_data['zones'].append(json_zone)

      cv_img = cv2.imread(img_path2, 1)
      open_cv_window()


   json_file.seek(0)
   json.dump(json_data, json_file, indent=4)
   json_file.close()

   cv2.waitKey(0)
   cv2.destroyAllWindows()
   