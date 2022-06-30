
import time
from src.models.Price import Price
from src.models.ItemQuantity import ItemQuantity
from src.models.Menu.Menu import Menu, Onglet, OngletEnum
from src.utils.screen_utils import ScreenArea, ScreenPos, click_on_search_delete, get_recipe_from_item, getStringFromPos, write_string
from src.utils.string_utils import StringUtils
from pykeyboard import PyKeyboard

from pymouse import PyMouse
from pykeyboard import PyKeyboard
from pynput.keyboard import Key, Controller


class Hdv(Menu):
    search_bar=ScreenPos(393,218)
    first_item=ScreenPos(640,246)
    one_pack=ScreenPos(987,282)
    ten_pack=ScreenPos(997,322)
    hundred_pack=ScreenPos(997,367)
    search_delete=ScreenPos(485,221)
    exit=ScreenPos(1066,112)
    one_price=ScreenArea(804,273,92,28)
    ten_price=ScreenArea(804,312,92,28)
    hundred_price=ScreenArea(804,354,92,28)
    confirm_purchase=ScreenArea(739,612,120,20)
    unit_price=ScreenArea(678,526,120,20)
    already_bought=ScreenArea(20,934,30,20)
    three_seconds=ScreenArea(750,608,20,16)

    
    def __init__(self):
            super().__init__("HDV",[Onglet(OngletEnum.ACHAT,ScreenPos(604,150)),Onglet(OngletEnum.VENTE,ScreenPos(768,159))])

    def buy_x_of_item(self,itemQuantity)->Price:
        keyboard = Controller()
        k = PyKeyboard()
        self.write_into_search_bar(itemQuantity)
        self.first_item.click(1)
        quantity=int(itemQuantity.quantite)
        total_price=0
        hundred_price=self.hundred_price.getIntFromScreenArea( "./assets/img/test/hundred_price.png")
        ten_price=self.hundred_price.getIntFromScreenArea( "./assets/img/test/ten_price.png")
        one_price=self.hundred_price.getIntFromScreenArea( "./assets/img/test/one_price.png")

        total_price_moy=min([hundred_price/100,ten_price/10,one_price])*quantity

        pack_mode=""
        while quantity!=0:
            if quantity/100 >=1 :
                self.hundred_pack.click(0.7)
                quantityAVirer=100
                prix_a_ajouter=hundred_price
                pack_mode="h"
            elif quantity/10 >=1:
                self.ten_pack.click(0.7)
                quantityAVirer=10
                prix_a_ajouter=ten_price
                pack_mode="t"
            else:
                self.one_pack.click(0.7)
                quantityAVirer=1
                prix_a_ajouter=one_price
                pack_mode="u"


            prixU=StringUtils.remove_shit(getStringFromPos(678,526,120,20,'./assets/img/test/prix_un.png'))
            if prixU=="Prixunitaire:":
                self.confirm_purchase.click(0.7)
            if StringUtils.remove_shit(getStringFromPos(49,935,70,15,'./assets/img/test/cetol.png'))!="objetn'est":
                quantity-=quantityAVirer
                total_price+=prix_a_ajouter
            else:
                print("déjà acheté")
                pack_mode="x"
                time.sleep(1)
                pass
        return Price(total_price,total_price_moy)         
    def buy_item(self,itemQuantity:ItemQuantity):
        time.sleep(2)
        price_item=0
        price_item_moy=0
        item_complete=itemQuantity.item.list_craft
        #item_complete=get_recipe_from_item(itemQuantity.item)
        
        for compItemQuantity in item_complete:
            compItemQuantity.quantite=compItemQuantity.quantite*itemQuantity.quantite
        for compItemQuantity in item_complete:
            price=self.buy_x_of_item(compItemQuantity)
            price_item+=price.price
            price_item_moy+=price.pricemoy
            click_on_search_delete()
    def write_into_search_bar(self,itemQuantity):
        self.search_delete.click(0.2)
        self.search_bar.click(0.2)
        write_string(StringUtils.strip_accents( itemQuantity.item.item_name))
        time.sleep(2.5)

