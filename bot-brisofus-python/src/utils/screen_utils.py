

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

from src.models.Item import Item
from src.models.ItemQuantity import ItemQuantity
from src.utils.string_utils import StringUtils
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import TimeoutException

m = PyMouse()
k = PyKeyboard()

def click_somewhere(x_pos,y_pos):
    m.click(x_pos, y_pos, 1)
    time.sleep(0.3)


def get_recipe_from_item(item:Item):

    return []




def getStringFromPos(x_pos,y_pos,width,height,path):
    monitor = {"top": y_pos, "left": x_pos, "width": width, "height": height}
    output = path.format(**monitor)
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    image = Image.open(path)

    test=pytesseract.image_to_string(PIL.ImageOps.invert(image))
    return test



def screenshot(x_pos,y_pos,width,height,path):
    monitor = {"top": y_pos, "left": x_pos, "width": width, "height": height}
    output = path.format(**monitor)
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    


#item 640 246
#1 PACK 987 282
#10 PACK 997 285
#100 PACK 997 367

def click_on_search_bar():
    click_somewhere(380,216)

def click_on_item():
    click_somewhere(640,246)

def click_on_1_pack():
    click_somewhere(987,282)

def click_on_10_pack():
    click_somewhere(999,329)

def click_on_100_pack():
    click_somewhere(992,371)

def click_on_search_delete():
    click_somewhere(485,221)

def click_somewhere_pos(pos):
    click_somewhere(pos.x,pos.y)

def click_somewhere_pos_double(pos):
    time.sleep(0.1)
    m.click(pos.x, pos.y, 1)



keyboard = Controller()

def write_string(string):
    time.sleep(0.2)
    k.type_string(string)

def press_enter():
    k.press_key("Return")



def image_pixel_differences(base_image, compare_image):
  base_image = Image.open(base_image)
  compare_image = Image.open(compare_image)
  diff = ImageChops.difference(base_image, compare_image)
  if diff.getbbox():
    return False
  else:
    return True





def get_item(item_id):
    with open("./assets/data.json") as f:
        objects = json.load(f)
    for item in objects:
        if item.item_id==item_id:
            return item



class ScreenPos(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def click(self,waiting_time):
        m.click(self.x, self.y, 1)
        time.sleep(waiting_time)


class ScreenArea(ScreenPos):
    def __init__(self, x, y,width,height):
        super().__init__(x,y)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def click(self,waiting_time):
        m.click(self.x, self.y, 1)
        time.sleep(waiting_time)
    def getStringFromScreenArea(self,path):
        screenshot(0,0,1679,1049,path)
        return self.getStringFromExistingScreen(path)
    def getIntFromScreenArea(self,path):
        screenshot(0,0,1679,1049,path)
        return self.getIntFromExistingScreen(path)
    def getStringCleanedFromScreen(self,path):
        return StringUtils.remove_shit(self.getStringFromScreenArea(path))
    def getStringCleanedFromExistingScreen(self,path):
        return StringUtils.remove_shit(self.getStringFromExistingScreen(path))
    def getStringFromExistingScreen(self,path,is_number=False):
        image = Image.open(path)
        image=image.crop((self.x*2, self.y*2, (self.x+self.width)*2, (self.y+self.height)*2))
        if is_number:
            return pytesseract.image_to_string(PIL.ImageOps.invert(image), config="--psm 6 digits")
        else:    
            return pytesseract.image_to_string(PIL.ImageOps.invert(image))
    def getIntFromExistingScreen(self,path):
        try :
            return int(StringUtils.remove_shit(self.getStringFromExistingScreen(path,is_number=True)))
        except ValueError:
            return 99999999999




