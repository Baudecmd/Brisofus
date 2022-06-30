
import json
import sys
from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from flask import request
from collections import namedtuple
from src.utils.string_utils import StringUtils
from src.utils.screen_utils import ScreenArea, ScreenPos, click_on_search_delete, get_recipe_from_item, getStringFromPos, write_string

import jsonpickle

from src.map_tile import Game, MapPoint
from src.models.Item import Item
from src.models.ItemQuantity import ItemQuantity

app = Flask(__name__)
game =Game(MapPoint.HDV_RESSOURCE_BONTA)
CORS(app, support_credentials=True)
def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap

class JsonUtils:
    def return_item_from_json_list(json):
        return [Item(**ob) for ob in json]
    def item_list_from(list_item):
        return json.dumps([ob.__dict__ for ob in list_item])


@app.route('/item/comp_buy',methods=['POST'])
def buy_items(): 
    items = request.get_json(silent=True)
    for i in items:
        print(items)
    response = jsonify(game.buy_craft_briser([JSONtoItemQuantity(item) for item in items]))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def JSONtoItemQuantity(json):
    print(json)
    itemQ=ItemQuantity()
    itemQ.quantite=json["quantite"]
    itemQ.item=Item()
    itemQ.item.item_name=json["resourceItem"]["name"]
    itemQ.item.item_type=json["resourceItem"]["type"]
    itemQ.item.list_craft=[]
    for i in json["resourceItem"]["listCraftResources"]:
        itemQ2=ItemQuantity()
        itemQ2.item=Item()
        itemQ2.item.item_name=i["resourceItem"]["name"]
        itemQ2.quantite=i["quantite"]
        itemQ.item.list_craft.append(itemQ2)
        print(i)
    return itemQ
    
print(getStringFromPos(49,935,70,15,'./assets/img/test/cetol.png'))

print("'"+StringUtils.remove_shit(getStringFromPos(49,935,70,15,'./assets/img/test/cetol.png'))+"'")
