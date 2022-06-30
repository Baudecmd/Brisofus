import re
import string
import unicodedata


class StringUtils:
    def strip_accents(text):
        try:
            text = re.UNICODE(text, 'utf-8')
        except (TypeError, NameError): # unicode is a default on python 3 
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)
    def get_price(string:string)->int:
        try:
            value=int(string)
            return value
        except ValueError:
            return 1
    def remove_shit(text):
        if text.replace("\n\x0c","").replace(".","").replace(" ","").replace("\n","").replace("\x0c","").isalpha()==False:
            if text.replace("\n\x0c","").replace(".","").replace(" ","").replace("\n","").replace("\x0c","")=="":
                return "9999999999"
            else:
                return text.replace("\n\x0c","").replace(".","").replace(" ","").replace("\n","").replace("\x0c","")
        else:
            return "9999999999"
    def remove_key_word_from_item_name(item_name):
        return item_name.replace(" de","").replace(" du","").replace("Ceinture","").replace("Bottes","").replace("Cape","").replace("Chapeau","").replace("Epee","").replace("Pelle","").replace("Anneau","").replace("Amulette","")

