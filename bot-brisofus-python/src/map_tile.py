from enum import Enum, auto
from logging import exception
import numpy as np
from PIL import ImageGrab
import pytesseract
from PIL import Image
import time
import requests
from PIL import Image
import PIL.ImageOps  
import mss
import mss.tools
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import re
import unicodedata
import pyautogui
from PIL import Image
from PIL import ImageChops
import math
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import re
import json
from typing import List, Set, Dict, Tuple, Optional
from src.models.Item import Item
from src.models.Menu.Craft import Craft
from src.models.Menu.HDV import Hdv
from src.models.Menu.Menu import OngletEnum
from src.models.Menu.Zappy import Zappy

from src.models.ItemQuantity import ItemQuantity
from src.utils.string_utils import StringUtils
from src.utils.screen_utils import ScreenPos, click_somewhere_pos, write_string





m = PyMouse()
k = PyKeyboard()

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TileAvecZappy(Tile):

    def __init__(self, x, y, zappy_screen_pos,zappy_name,zappy_onglet):
        self.zappy_onglet=zappy_onglet
        super().__init__(x, y)
        self.zappy_screen_pos=zappy_screen_pos
        self.zappy_name=zappy_name

class TileAvecHDV(TileAvecZappy):
    def __init__(self,x,y,zappy_screen_pos,hdv_screen_pos,zappy_name,zappy_onglet):
        super().__init__(x,y,zappy_screen_pos,zappy_name,zappy_onglet=zappy_onglet)
        self.hdv_screen_pos=hdv_screen_pos

class TileAtelier(TileAvecZappy):
    def __init__(self,x,y,zappy_screen_pos,atelier_screen_pos,zappy_name,zappy_onglet,atelier_etabli_screen_pos,sortie_atelier_screen_pos):
            super().__init__(x,y,zappy_screen_pos,zappy_name,zappy_onglet=zappy_onglet)
            self.atelier_screen_pos=atelier_screen_pos  
            self.sortie_atelier_screen_pos=sortie_atelier_screen_pos
            self.atelier_etabli_screen_pos=atelier_etabli_screen_pos

class TileHdvRune(TileAvecHDV):
    def __init__(self,x,y,zappy_screen_pos,hdv_screen_pos,atelier_screen_pos,zappy_name, zappy_onglet, atelier_etabli_screen_pos, sortie_atelier_screen_pos):
            super().__init__(x=x,y=y,zappy_screen_pos=zappy_screen_pos,zappy_name=zappy_name,zappy_onglet=zappy_onglet,hdv_screen_pos=hdv_screen_pos)
            self.atelier_screen_pos=atelier_screen_pos  
            self.sortie_atelier_screen_pos=sortie_atelier_screen_pos
            self.atelier_etabli_screen_pos=atelier_etabli_screen_pos

   

    
    

class ListMenu:
    ZAPPY=Zappy()
    HDV=Hdv()
    CRAFT=Craft()

class MapPoint:
    ZAAP_BONTA = TileAvecZappy(zappy_onglet=OngletEnum.DIVERS,zappy_name="zaap",x=-31,y=-56,zappy_screen_pos=ScreenPos(x=1245,y=207))
    HDV_RESSOURCE_BONTA = TileAvecHDV(zappy_onglet=OngletEnum.HOTEL_DES_VENTES,zappy_name="hotel de vente des ress",x=-30,y=-54,zappy_screen_pos=ScreenPos(x=627,y=301),hdv_screen_pos=ScreenPos(x=1362,y=452))
    HDV_RUNES_BONTA = TileHdvRune(zappy_onglet=OngletEnum.HOTEL_DES_VENTES,zappy_name="hotel de vente des runes",x=-29,y=-57,zappy_screen_pos=ScreenPos(x=1195,y=90),atelier_screen_pos=ScreenPos(989,556),hdv_screen_pos=ScreenPos(x=1349,y=604),sortie_atelier_screen_pos=ScreenPos(1112,614),atelier_etabli_screen_pos=ScreenPos(721,584))
    ATELIER_CORDONNIER = TileAtelier(zappy_onglet=OngletEnum.ATELIERS,zappy_name="atelier des cordo",x=-30,y=-57,zappy_screen_pos=ScreenPos(x=1192,y=282),atelier_screen_pos=ScreenPos(864,335),sortie_atelier_screen_pos=ScreenPos(1182,508),atelier_etabli_screen_pos=ScreenPos(791,509))
    ATELIER_TAILLEUR = TileAtelier(zappy_onglet=OngletEnum.ATELIERS,zappy_name="atelier des taill",x=-30,y=-57,zappy_screen_pos=ScreenPos(x=332,y=426),atelier_screen_pos=ScreenPos(819,722),sortie_atelier_screen_pos=ScreenPos(451,793),atelier_etabli_screen_pos=ScreenPos(787,691))
    ATELIER_BIJOUTIER = TileAtelier(zappy_onglet=OngletEnum.ATELIERS,zappy_name="atelier des bijout",x=-33,y=-55,zappy_screen_pos=ScreenPos(x=579,y=570),atelier_screen_pos=ScreenPos(858,527),sortie_atelier_screen_pos=ScreenPos(1029,675),atelier_etabli_screen_pos=ScreenPos(888,591))
    ATELIER_FORGERON = TileAtelier(zappy_onglet=OngletEnum.ATELIERS,zappy_name="atelier des forger",x=-30,y=-56,zappy_screen_pos=ScreenPos(x=682,y=636),atelier_screen_pos=ScreenPos(829,517),sortie_atelier_screen_pos=ScreenPos(1014,787),atelier_etabli_screen_pos=ScreenPos(603,603))
    ATELIER_SCULPTEUR = TileAtelier(zappy_onglet=OngletEnum.ATELIERS,zappy_name="sculpteurs",x=-33,y=-55,zappy_screen_pos=ScreenPos(x=527,y=224),atelier_screen_pos=ScreenPos(800,600),sortie_atelier_screen_pos=ScreenPos(500,700),atelier_etabli_screen_pos=ScreenPos(655,400))

class Game:
    def __init__(self,starting_point):
        self.currentPos=starting_point
        self.listMenu=[]
    
    def goToMap(self,map):
        time.sleep(3)
        self.currentPos.zappy_screen_pos.click(0)
        time.sleep(4)
        ListMenu.ZAPPY.getOnglet(map.zappy_onglet).position.click(0)
        time.sleep(0.5)
        ListMenu.ZAPPY.search_bar.click(0)
        time.sleep(0.5)
        write_string(map.zappy_name)
        time.sleep(2)
        ListMenu.ZAPPY.first_zaap.click(0)
        time.sleep(0.5)
        ListMenu.ZAPPY.bouton_teleportation.click(0)
        self.setCurrentPos(map)

    def buy_x_item(self,list_of_item_quantity:List[ItemQuantity]):
        if self.currentPos!=MapPoint.HDV_RESSOURCE_BONTA:
            self.goToMap(MapPoint.HDV_RESSOURCE_BONTA)
        time.sleep(5)
        MapPoint.HDV_RESSOURCE_BONTA.hdv_screen_pos.click(2)
        for item_quantity in list_of_item_quantity:
            ListMenu.HDV.buy_item(item_quantity)
        time.sleep(1)
        ListMenu.HDV.exit.click(0)


    def get_atelier_from_item(self,item:Item):
        type=item.item_type
        if type in ["Ceinture","Bottes"]:
            return MapPoint.ATELIER_CORDONNIER
        elif type in ["Amulette","Anneau"]:
            return MapPoint.ATELIER_BIJOUTIER
        elif type in ["Cape","Chapeau"]:
            return MapPoint.ATELIER_TAILLEUR
        elif type in ["Baguette","Bâton"]:
            return MapPoint.ATELIER_SCULPTEUR
        else:
            return MapPoint.ATELIER_FORGERON

    def craft_x_item(self,list_of_item_quantity:List[ItemQuantity]):

        atelier=self.get_atelier_from_item(list_of_item_quantity[0].item)

        if self.currentPos!=atelier:
            self.goToMap(atelier)
        
        time.sleep(2)
        atelier.atelier_screen_pos.click(4)
        atelier.atelier_etabli_screen_pos.click(3.5)
        ListMenu.CRAFT.uniquement_possible.click(0)
        list_craft=0
        for itemQuantity in list_of_item_quantity:
            time.sleep(0.5)
            ListMenu.CRAFT.write_into_search_bar(itemQuantity=itemQuantity)
            time.sleep(2)
            ListMenu.CRAFT.premier_craft.click(1)
            ListMenu.CRAFT.nombre_de_craft.click(0.2)
            ListMenu.CRAFT.max_craft.click(0.2)
            ListMenu.CRAFT.ok_craft.click(0.2)
            ListMenu.CRAFT.faire_craft.click(1)
            list_craft+=1
        ListMenu.CRAFT.exit.click(1)
        atelier.sortie_atelier_screen_pos.click(3)
    
    def brisage_x_item(self,list_of_item):
        if self.currentPos!=MapPoint.HDV_RUNES_BONTA:
            self.goToMap(MapPoint.HDV_RUNES_BONTA)
        time.sleep(4)
        click_somewhere_pos(MapPoint.HDV_RUNES_BONTA.atelier_screen_pos)
        time.sleep(5)
        click_somewhere_pos(MapPoint.HDV_RUNES_BONTA.atelier_etabli_screen_pos)
        
    def buy_craft_briser(self,list_of_item_quantity):
        self.buy_x_item(list_of_item_quantity)
        self.craft_x_item(list_of_item_quantity)
        self.brisage_x_item(list_of_item_quantity)
    
    def setCurrentPos(self,nextPos):
        self.currentPos=nextPos

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Item):
            return obj.__dict__         # <-----
        return json.JSONEncoder.default(self, obj)

