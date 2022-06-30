
import json
import re
from telnetlib import EC
import time
from typing import List
import urllib.request
from bs4 import BeautifulSoup
import urllib3
from src.models.Stat import Stat
from src.models.ItemQuantity import ItemQuantity
from src.map_tile import ComplexEncoder

from src.models.Item import Item
from src.utils.screen_utils import get_recipe_from_item
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import jsonpickle
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Firefox()
def get_recipe2_from_item(item:Item):
    driver.get("https://www.dofusbook.net/fr/encyclopedie/objet/"+str(item.item_id))

    list_stat:List[Stat]=[]
    content = driver.page_source
    soup = BeautifulSoup(content,features='html.parser')  

    list_stat_html=soup.find_all("span",class_="pl-2")

    for stat_html in list_stat_html:
        string_cleaned=stat_html.text[1:-1]
        print(string_cleaned)
        stat_local=re.findall(r'\d+',string_cleaned)
        try:
            if 'à' in string_cleaned:
                list_stat.append(Stat(int(" ".join(string_cleaned.split(' ')[3:])),min=stat_local[0],max=stat_local[1]))

            else:
                list_stat.append(Stat(int(" ".join(string_cleaned.split(' ')[1:])),min=stat_local[0],max=stat_local[0]))
        except:
            print("error")
    item.list_stat=list_stat

    try:
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[5]/div[3]/div[2]/div[1]/div/div[3]/div/div")))
        
        element.click()
        time.sleep(1)
        content = driver.page_source
        soup = BeautifulSoup(content,features='html.parser')  


        results=soup.find_all("div", class_="ingredient")
        item_name=soup.find("div", class_="title").find("a").text
        list_item=[]
        quantity=0
        for text in results:
            img_id=int(re.findall(r'\d+',text.find("img")['src'])[0])
            full_string=text.find("div",class_="ingredient-name").text
            full_string=full_string[1:len(full_string)]
            for element in range(0, len(full_string)):
                if full_string[element] not in ['0','1','2','3','4','5','6','7','8','9']:
                    quantity=int(full_string[0:element])
                    item_name=full_string[element+1:len(full_string)-1]
                    break
            list_item.append(ItemQuantity(item=Item(item_id=0,item_name=item_name,item_type="",img_id=img_id,list_craft=[],list_stat=[],level=0),quantite=quantity))
        item.list_craft=list_item
    except:
        pass
    return item


def read_all_item():
    #driver.get("https://www.dofusbook.net/fr/encyclopedie/objet/"+str(item_id))
    list_item=[]

    list_item.extend(read_all_item_from_html_file("./assets/scrapping/amulette.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/anneau.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/bottes.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/cape.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/ceinture.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/chapeau.html"))

    i=0
    for item in list_item:
        print(item)
        i+=1
        item=get_recipe2_from_item(item)
    json_string = jsonpickle.encode(list_item)
    text_file = open("./assets/test_data.json", "w")
    text_file.write(json_string)
    text_file.close()
    driver.close()


def read_all_item_from_html_file(path):
    f = open(path, "r")
    amulette=f.read()
    soup = BeautifulSoup(amulette,features='html.parser')  
    list_item=[]
    results=soup.find_all("div", class_="col-sm-12 col-lg-8 px-3 pb-6")
    for i in results:
        item_name=i.find("h3", class_="title").text
        item_name=item_name[1:len(item_name)-1]
        item_id=int(re.findall(r'\d+', i.find("a",href=True,class_="link-white")['href'])[0])
        item_level=int(re.findall(r'\d+', i.find("div",class_="subtitle").text)[0])
        item_type=i.find("div",class_="subtitle").text.replace("-","").replace(" ","").replace("Niveau","").replace(str(item_level),"")
        img_id=int(re.findall(r'\d+', i.find("div",class_="thumbnail").find("img",src=True)['src'])[0])
        list_item.append(Item(level=item_level,item_name=item_name,list_stat=[],list_craft=[],item_id=item_id,item_type=item_type,img_id=img_id))
    return list_item

read_all_item()