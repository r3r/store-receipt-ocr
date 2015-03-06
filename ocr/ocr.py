import sys
sys.path.append("Lib/site-packages")

from pytesser.pytesser import *
from PIL import Image
import cStringIO
from base64 import b64encode, b64decode
import re


class ReceiptOCR():

    def __init__(self, image_64):
        self.image_64 = image_64
        try:
            self.image = Image.open(cStringIO.StringIO(b64decode(image_64)))
        except TypeError:
            raise Exception("Could not decode base64 data")


    def convert_to_text(self):
        return image_to_string(self.image)

    def get_structure(self):
        text = self.convert_to_text()
        arr_text = text.split('\n')
        ret = dict()
        for txt in arr_text:
            if self.grocery_item(txt): #to stop processing after Subtotal/Total etc.
                re1='.*?'	# Non-greedy match on filler
                re2='(\\$?[0-9]+(?:\\.[0-9][0-9])?)(?![\\d])'	# Dollar Amount 1
                rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
                m = rg.search(txt)
                if m: #only if dollar amount found
                    dollars=m.group(1)
                    ind = txt.rindex(dollars)
                    txt = txt[:ind]
                    if txt:
                        ret[txt] = dollars
            else:
                break
        return ret

    def grocery_item(self, txt):
        sentinels = ['total', 'subtotal', 'balance', 'tax', 'change', 'sub-total' ]
        txt = txt.lower()
        for sentinel in sentinels:
            if sentinel in txt:
                return False
        return True



def test():
    f = open('bill2.jpg', 'rb')
    j = b64encode(f.read())
    print len(j)
    f.close()
    f = open('bill_base64.txt', 'w')
    f.write(j)
    f.close()
    #ocr = ReceiptOCR(j)
    #print ocr.convert_to_text()

if __name__=="__main__":
    test()
