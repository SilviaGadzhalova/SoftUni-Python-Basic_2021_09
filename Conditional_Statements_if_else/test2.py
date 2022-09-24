import pyqrcode
import png
from pyqrcode import QRCode

link = "https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11632226325027018&slink=ln8y2z"
url = pyqrcode.create(link)
url.png ("qr.png", scale = 8)


