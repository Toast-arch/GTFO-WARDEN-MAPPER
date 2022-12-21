import json
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

##CLASSES
class ID_:
    def __init__(self, index=0, seed=0, area='', x=0, y=0, z=0, lock=0, islocker=True):
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

    def draw_container(self, background, locker_png, box_png):
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
    def __init__(self, name, index, type, idlist, image_file, package_name):
        self.name_ = name
        self.index_ = index
        self.type_ = type
        self.idlist_ = idlist
        self.image_file_ = image_file
        self.image_ = Image.open("packages/" + package_name + '/' + image_file)
    
    def save_image(self):
        self.image_.save(self.image_file_[:len(self.image_file_) - 4] + "_GENERATED.png")

class ARG_:
    def __init__(self, key, sub_list=[]):
        self.key_ = key
        self.sub_list_ = sub_list
