import json
import re

from bs4 import BeautifulSoup
from src.map_tile import ComplexEncoder
from src.models.Item import Item


def read_all_item():
    #driver.get("https://www.dofusbook.net/fr/encyclopedie/objet/"+str(item_id))
    list_item=[]

    list_item.extend(read_all_item_from_html_file("./assets/scrapping/amulette.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/anneau.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/bottes.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/cape.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/ceinture.html"))
    list_item.extend(read_all_item_from_html_file("./assets/scrapping/chapeau.html"))


    for item in list_item:
       print(item)
    json_string = json.dumps([ob.__dict__ for ob in list_item],cls=ComplexEncoder)
    text_file = open("./assets/data.json", "w")
    
    #write string to file
    text_file.write(json_string)
    
    #close file
    text_file.close()

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

