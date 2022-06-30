from filecmp import clear_cache
from telethon import TelegramClient, events, sync
import re
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
from playsound import playsound
from selenium import webdriver
card_var=''
from selenium.common.exceptions import NoSuchElementException       

from enum import Enum






def check_exists_by_xpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


class AnyEc:
    """ Use with WebDriverWait to combine expected_conditions
        in an OR.
    """
    def __init__(self, *args):
        self.ecs = args
    def __call__(self, driver):
        for fn in self.ecs:
            try:
                res = fn(driver)
                if res:
                    return True
                    # Or return res if you need the element found
            except:
                pass


# Remember to use your own values from my.telegram.org!
api_id =  15096703 
api_hash = '2ead79f20265865068b6501887d2df9d'
client = TelegramClient('anon', api_id, api_hash)

list_of_wanted_gpu=["RTX 3070","RTX 3070 Ti","RTX 3060","RTX 3060 Ti"]

def Find(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]

@client.on(events.NewMessage(chats='🔥 FE PartAlert'))
async def my_event_handler(event):
    print(event.raw_text)
    processThread = threading.Thread(target=process_gpu_event, args=(event,))  # <- note extra ','
    processThread.start()
    

def process_gpu_event(event):
    for gpu in list_of_wanted_gpu:
            if gpu in event.raw_text and "(FR)" in event.raw_text:
                url=Find(event.raw_text)[0]
                if "RTX 3070" in event.raw_text and "Ti" not in event.raw_text :
                    buy2(url)
                elif "RTX 3060" in event.raw_text:
                    buy2(url)
                else:
                    print("pas vouloir ça moi")

def click_element_optional(driver,xpath): 
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def click_element(driver,xpath):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def fill_field(driver,xpath,value):
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.send_keys(value)

def click_one_or_the_other(driver,xpath1,xpath2):
    element= WebDriverWait(driver, 30).until( AnyEc(
    EC.presence_of_element_located(
         (By.XPATH,xpath1)),
    EC.presence_of_element_located(
         (By.XPATH,xpath2)) ))
    if check_exists_by_xpath(driver,xpath1):
        driver.find_element_by_xpath(xpath1).click()
    else:
        driver.find_element_by_xpath(xpath2).click()


def buy2(url):
    driver = webdriver.Firefox()
    driver.get(url)
    click_element(driver,'//*[@id="cookieConsentAcceptButton"]')
    click_one_or_the_other(driver,'/html/body/div[4]/div[2]/div[2]/div[3]/aside/div[3]/div[2]/button[1]', '/html/body/div[4]/div[2]/div[2]/div[3]/aside/div[4]/div[2]/button[1]')             
    click_one_or_the_other(driver,'/html/body/div[15]/div/div/div/div[1]/div[2]/div[3]/a','/html/body/div[16]/div/div/div/div[1]/div[2]/div[3]/a')  
    click_one_or_the_other(driver,'/html/body/section/div[1]/div/div/div/div[2]/aside/div[4]/form/button','    /html/body/section/div[1]/div/div/div/div[2]/aside/div[6]/form/button')
    try:
        click_element_optional(driver,'/html/body/div[10]/div/div/div[2]/div[4]/div/div[2]/a')
    except:
        pass
    fill_field(driver,'//*[@id="Email"]','conradbaudelet@gmail.com')
    fill_field(driver,'//*[@id="Password"]','Xldt3950.')
    click_element(driver,'/html/body/div[3]/div/form/button')
    click_element(driver,'/html/body/div[3]/div/div[3]/div/div[1]/form/div[1]')
    time.sleep(0.5)
    fill_field(driver,'//*[@id="CardNumber"]',card_var)
    fill_field(driver,'//*[@id="ExpirationDate"]','0224')
    fill_field(driver,'//*[@id="OwnerName"]','Conrad BAUDELET')
    fill_field(driver,'//*[@id="Cryptogram"]','909')
    click_element(driver,'/html/body/div[3]/div/div[4]/div[2]/div[1]/div/div/form/div[8]/div/button')


#buy2("https://www.ldlc.com/fiche/PB00355643.html")
client.start()
print("Programme démarré")
client.run_until_disconnected()     
