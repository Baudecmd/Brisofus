import time
import unittest
from src.map_tile import ListMenu

from src.utils.screen_utils import getStringFromPos, screenshot


class TestStringMethods(unittest.TestCase):

    def test_already_bought(self):
        price=ListMenu.HDV.already_bought.getStringCleanedFromExistingScreen("./assets/img/unittest/already_bought.png")
        self.assertEqual("Cetot",price)
    def test_hundred_price(self):
        hundred=ListMenu.HDV.hundred_price.getIntFromExistingScreen("./assets/img/unittest/one_price0.png")
        ten=ListMenu.HDV.ten_price.getIntFromExistingScreen("./assets/img/unittest/one_price0.png")
        one=ListMenu.HDV.one_price.getIntFromExistingScreen("./assets/img/unittest/one_price0.png")
        self.assertEqual(99990,hundred)
        self.assertEqual(8976,ten)
        self.assertEqual(928,one)
    def test_one_price2(self):
        hundred=ListMenu.HDV.hundred_price.getIntFromExistingScreen("./assets/img/unittest/one_price1.png")
        ten=ListMenu.HDV.ten_price.getIntFromExistingScreen("./assets/img/unittest/one_price1.png")
        one=ListMenu.HDV.one_price.getIntFromExistingScreen("./assets/img/unittest/one_price1.png")
        self.assertEqual(1,one)
        self.assertEqual(100,ten)
        self.assertEqual(958,hundred)
    def test_one_price2(self):
        hundred=ListMenu.HDV.hundred_price.getIntFromExistingScreen("./assets/img/unittest/one_price2.png")
        ten=ListMenu.HDV.ten_price.getIntFromExistingScreen("./assets/img/unittest/one_price2.png")
        one=ListMenu.HDV.one_price.getIntFromExistingScreen("./assets/img/unittest/one_price2.png")
        self.assertEqual(930,one)
        self.assertEqual(6667,ten)
        self.assertEqual(55808,hundred)
    def test_one_price3(self):
        hundred=ListMenu.HDV.hundred_price.getIntFromExistingScreen("./assets/img/unittest/one_price3.png")
        ten=ListMenu.HDV.ten_price.getIntFromExistingScreen("./assets/img/unittest/one_price3.png")
        one=ListMenu.HDV.one_price.getIntFromExistingScreen("./assets/img/unittest/one_price3.png")
        self.assertEqual(90,one)
        self.assertEqual(898,ten)
        self.assertEqual(13800,hundred)
    def test_one_price4(self):
        hundred=ListMenu.HDV.hundred_price.getIntFromExistingScreen("./assets/img/unittest/one_price4.png")
        ten=ListMenu.HDV.ten_price.getIntFromExistingScreen("./assets/img/unittest/one_price4.png")
        one=ListMenu.HDV.one_price.getIntFromExistingScreen("./assets/img/unittest/one_price4.png")
        self.assertEqual(900,one)
        self.assertEqual(13484,ten)
        self.assertEqual(99999,hundred)
    def test_confirm_purchase_presence(self):
        price=ListMenu.HDV.unit_price.getStringCleanedFromExistingScreen("./assets/img/unittest/confirm_purchase.png")
        self.assertEqual("Prixunitaire:",price)
    def test_3_seconds(self):
        price=ListMenu.HDV.three_seconds.getIntFromExistingScreen("./assets/img/unittest/ooooo.png")
        self.assertEqual(2,price)



    

if __name__ == '__main__':
    unittest.main()