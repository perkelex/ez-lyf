from PIL import Image, ImageDraw, ImageFont
from PySide6.QtGui import *

class TrayIcon(QIcon):
    def __init__(self, path, week):
        super().__init__(path)
        self.ico = None
        self.drawIco(week)
        self.saveIco(path)

    def drawIco(self, text):
        self.ico= Image.new("RGB", (256, 256), color = (0, 0, 0))

        img = ImageDraw.Draw(self.ico)
        fnt = ImageFont.truetype("arial.ttf", 230)
        green = (0, 255, 0)
        if int(text) < 10:
            img.text((60,0), str(text), font=fnt, fill=green)
        else:
            img.text((0,0), str(text), font=fnt, fill=green)

    def saveIco(self, path):
        self.ico.save(path)