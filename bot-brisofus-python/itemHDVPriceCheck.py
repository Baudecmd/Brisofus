import numpy as np
from PIL import ImageGrab
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from textblob import TextBlob
import time
from pynput.mouse import Button, Controller
import requests
import unidecode
from PIL import Image
import PIL.ImageOps  
import mss
import mss.tools

mouse = Controller()

def getStringFromPos(x_pos,y_pos,path):
    monitor = {"top": y_pos, "left": x_pos, "width": 220, "height": 35}
    output = path.format(**monitor)
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    image = Image.open(path)

    test=pytesseract.image_to_string(PIL.ImageOps.invert(image))
    return test
old_name=""

for i in range(0,15000):
    nom=getStringFromPos(580,265,'nom_'+'.png')
    if(nom!=old_name):
        print("//////////////")

        old_name=nom
        print(nom)
        data=requests.get("http://localhost:8080/priceCraftItem/name/"+nom.replace("\n\x0c","").replace(".","").replace(" ","").replace("\n",""))
        print(data.json().get("item").get("name"))
        print(" : ")
        print(data.json().get("price"))
        print("------")
        print(data.json())
    time.sleep(1)
    