from enum import Enum, auto
import json
import string


class Stat:
    def __init__(self,type:string,min:int,max:int):
        self.type=type
        self.min=min
        self.max=max

    def __repr__(self):
        return "{} (lvl {}) avec id {} avec le type {} avec {} en image id".format(self.item_name,self.level,self.item_id,self.item_type,self.img_id)


