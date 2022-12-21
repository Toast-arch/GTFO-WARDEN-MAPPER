import os
from PIL import Image
import json
import sys
import cv2
from assets.dataclasses import ID_, ZONE_, ARG_

def click_event(event, x, y, flags, params):
 
   if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
      print("Object x: ", x)
      print("Object y: ", y)
      print("- - - - - - - - -")
      global global_x
      global_x = x
      global global_y
      global_y = y

      global global_wasclicked
      global_wasclicked = True

      global global_leftclick
      global_leftclick = event == cv2.EVENT_LBUTTONDOWN

      cv2.destroyAllWindows()

def open_cv_window():
   global global_wasclicked
   global_wasclicked = False
   cv2.imshow('window42', cv_img)
   cv2.setMouseCallback('window42', click_event)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

def overwrite_image_PIL(open_path, save_path):
   background = Image.open(open_path)
   background.save(save_path)

def draw_container_on_image(findex, fx, fy, fz, flock, fislocker, fbackground_img_path, fsave):
   
   id = ID_(index=findex, x=fx, y=fy, z=fz, lock=flock, islocker=fislocker)

   background = Image.open(fbackground_img_path)

   id.draw_container(background=background, locker_png=locker_png, box_png=box_png)

   background.save(fsave)

if __name__=="__main__":
   #ARGUMENT READING
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

   package_name = arg_list[1].key_

   defaultz = False
   defaultlock = False
   autoindex = False
   auto_index_value = 0

   #ARGUMENT APPLY
   for arg in arg_list:
      if arg.key_ == '--defaultz':
         defaultz = True
      if arg.key_ == '--defaultlock':
         defaultlock = True
      if arg.key_ == '--autoindex':
         autoindex = True
         auto_index_value = int(arg.sub_list_[0])

   global global_x
   global_x = -1
   global global_y
   global_y = -1

   json_file = open(os.path.join("packages", package_name, package_name + '.json'), 'r+')

   json_data = json.load(json_file)

   ## LOADING PIL IMAGE ASSETS
   locker_png = Image.open("assets/locker.png")
   box_png = Image.open("assets/box.png")

   #CREATING NEW ZONE
   name = input("New zone name: ")
   index = int(input("New zone index: "))
   type = input("New zone type: ")
      
   while True:
      map_file = input("New zone map file: ")
      try_path = os.path.join("packages", package_name, map_file)

      if os.path.exists(try_path):
         break
      else:
         print(try_path + " does not exist.")

   json_zone = {
      "name": name,
      "index": index,
      "type": type,
      "map file": map_file,
      "data": []
   }

   #CREATING NEW OBJECTS
   number_of_objects = int(input("Number of objects: "))

   img_path = os.path.join("packages", package_name, map_file)
   img_path_preview = map_file[:-4] + "_preview.png"
   #img_path_preview2 = map_file[:-4] + "_preview2.png"
   img_path_fullpreview = map_file[:-4] + "_fullpreview.png"
   
   overwrite_image_PIL(img_path, img_path_preview)
   #overwrite_image_PIL(img_path, img_path_preview2)
   overwrite_image_PIL(img_path, img_path_fullpreview)

   for i in range(number_of_objects):
      print("NEW SEEDED CONTAINER: ")

      #INPUT INDEX
      if autoindex:
         print("Object index: " + str(auto_index_value))
         index = auto_index_value
         auto_index_value += 1
      else:
         while True:
            index = input("Object index: ")
            try:
               index = int(index)
               break
            except ValueError:
               print("Must be a valid number")

      #INPUT SEED
      while True:
         seed = input("Object seed: ")
         try:
            seed = int(seed)
            break
         except ValueError:
            print("Must be a valid number")
      
      area = input("Object area: ")

      #INPUT Z
      if defaultz:
         z = 0
      else:
         while True:
            z = input("Object z: ")
            try:
               z = int(z)
               break
            except ValueError:
               print("Must be a valid number")
      
      #INPUT LOCK
      if defaultlock:
         lock = 0
      else:
         while True:
            lock = input("Object lock: ")
            try:
               lock = int(z)
               break
            except ValueError:
               print("Must be a valid number")

      global global_wasclicked
      global_wasclicked = True

      while global_wasclicked:
         #overwrite_image_PIL(img_path_fullpreview, img_path_preview)

         cv_img = cv2.imread(img_path_preview, 1)
         open_cv_window()

         if not global_wasclicked:
            break

         draw_container_on_image(findex=index, fx=global_x, fy=global_y, fz=z, flock=lock, fislocker=global_leftclick, fbackground_img_path=img_path_fullpreview, fsave=img_path_preview)
      
      draw_container_on_image(findex=index, fx=global_x, fy=global_y, fz=z, flock=lock, fislocker=global_leftclick, fbackground_img_path=img_path_fullpreview, fsave=img_path_fullpreview)

      json_id = {
         "index": index,
         "seed": seed,
         "area": area,
         "x": global_x,
         "y": global_y,
         "z": z,
         "lock": lock,
         "islocker": global_leftclick
      }
      
      print("Last coordinates saved!")

      json_zone['data'].append(json_id)

   json_data['zones'].append(json_zone)

   json_file.seek(0)
   json.dump(json_data, json_file, indent=4)
   json_file.close()

   cv2.waitKey(0)
   cv2.destroyAllWindows()
   