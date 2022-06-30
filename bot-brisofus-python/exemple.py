import unittest

from src.utils.screen_utils import getStringFromPos, screenshot


class TestStringMethods(unittest.TestCase):

    def testhe(self):
        screenshot(0,0,1679,1049,"./assets/img/unittest/one_price4.png")

    

if __name__ == '__main__':
    unittest.main()