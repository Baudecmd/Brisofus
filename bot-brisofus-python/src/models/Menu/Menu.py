from enum import Enum, auto


class Menu(object):
    def __init__(self,name,list_onglet):
        self.name=name
        self.list_onglet=list_onglet

    def getOnglet(self,onglet_enum):
        for onglet in self.list_onglet:
            if onglet.ongletEnum == onglet_enum:
                return onglet

class Onglet:
    def __init__(self,ongletEnum,position):
        self.ongletEnum=ongletEnum
        self.position=position

class OngletEnum(Enum):
    ATELIERS=auto()
    HOTEL_DES_VENTES=auto()
    DIVERS=auto()
    ACHAT=auto()
    VENTE=auto()