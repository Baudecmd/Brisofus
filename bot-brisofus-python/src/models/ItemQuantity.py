import json

from src.models.Item import Item


class ItemQuantity:
    def __init__(self,item:Item,quantite:int):
        self.item=item
        self.quantite=quantite
    def __init__(self):
        pass