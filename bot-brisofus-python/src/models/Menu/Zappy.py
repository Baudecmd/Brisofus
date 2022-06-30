
from src.models.Menu.Menu import Menu, Onglet, OngletEnum
from src.utils.screen_utils import ScreenPos


class Zappy(Menu):
    first_zaap=ScreenPos(204,240)
    search_bar=ScreenPos(479,157)
    bouton_teleportation=ScreenPos(348,644)
    def __init__(self):
            super().__init__("ZAPPY",[Onglet(OngletEnum.ATELIERS,ScreenPos(109,112)),Onglet(OngletEnum.HOTEL_DES_VENTES,ScreenPos(277,112)),Onglet(OngletEnum.DIVERS,ScreenPos(439,112))])
                           
