import json


class Item:
    def __init__(self,item_id,item_name,list_stat,list_craft,level,item_type,img_id):
        self.item_id=item_id
        self.item_name=item_name
        self.list_stat=list_stat
        self.list_craft=list_craft
        self.level=level
        self.item_type=item_type
        self.img_id=img_id
    def __init__(self):
       pass
    def __repr__(self):
        return "{} (lvl {}) avec id {} avec le type {} avec {} en image id".format(self.item_name,self.level,self.item_id,self.item_type,self.img_id)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)