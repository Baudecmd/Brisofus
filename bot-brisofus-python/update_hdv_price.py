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
time.sleep(1)
def getStringFromPos(i_eme,path):
    monitor = {"top": 276+i_eme*36, "left": 612, "width": 235, "height": 35}
    output = path.format(**monitor)
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    image = Image.open(path)

    test=pytesseract.image_to_string(PIL.ImageOps.invert(image))
    return test

def getNumberFromPos(i_eme,path):
    monitor = {"top": 276+i_eme*36, "left": 1225, "width": 105, "height": 35}
    output = path.format(**monitor)
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    image = Image.open(path)

    test=pytesseract.image_to_string(PIL.ImageOps.invert(image))
    return test


def getItem2():
    column_height=72
    
    for i in range(0,8):
        

        try:
            nom=getStringFromPos(i,'nom_'+str(i)+'.png')
            prix=getNumberFromPos(i,'prix_'+str(i)+'.png')
            data = {"item":nom.replace("\n\x0c","").replace(".","").replace("\n",""), "price":int(prix.replace(" ", ""))}
            requests.post("http://localhost:8080/priceItem", json = data,timeout=0.0000000001)
        except requests.exceptions.ReadTimeout: 
            pass


            print(data)
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
 
def eachItem2():
    for i in range(0,15444):
        mouse.scroll(0,8)
        time.sleep(1)
        getItem2()


time.sleep(1)
eachItem2()

