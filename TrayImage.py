from PIL import Image, ImageDraw, ImageFont
from getpass import getuser

tray_ico_path = "C:\\Users\\" + getuser() + "\\AppData\\Local\\Temp\\currentWeek_icon.ico"

class TrayImage:
    def __init__(self):
        pass

    def draw(self, text):
        img = Image.new("RGB", (256, 256), color = (0, 0, 0))

        ico = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("arial.ttf", 230)
        green = (0, 255, 0)
        if int(text) < 10:
            ico.text((60,0), str(text), font=fnt, fill=green)
        else:
            ico.text((0,0), str(text), font=fnt, fill=green)


        img.save(tray_ico_path)
        return tray_ico_path