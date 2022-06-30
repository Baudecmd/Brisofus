

import time
from src.models.Menu.Menu import Menu
from src.utils.screen_utils import ScreenPos, write_string
from src.utils.string_utils import StringUtils
from pykeyboard import PyKeyboard


class Craft(Menu):
    uniquement_possible=ScreenPos(351,725)
    nombre_de_craft=ScreenPos(897,415)
    max_craft=ScreenPos(801,445)
    ok_craft=ScreenPos(994,446)
    faire_craft=ScreenPos(873,494)
    premier_craft=ScreenPos(429,256)
    exit=ScreenPos(1391,115)
    search_bar=ScreenPos(330,150)
    beginning_search_bar=ScreenPos(274,151)
    end_search_bar=ScreenPos(432,151)

    def __init__(self):
            super().__init__("CRAFT",[])

    def is_search_bar_blank():
        return True
    
    def write_into_search_bar(self,itemQuantity):
        k = PyKeyboard()
        self.end_search_bar.click(0.1)
        time.sleep(0.1)
        for i in range(0,30):
            k.press_key('delete')
            time.sleep(0.01)
            k.release_key('delete')
        time.sleep(0.3)
        write_string(StringUtils.strip_accents( itemQuantity.item.item_name[-8:]))
        