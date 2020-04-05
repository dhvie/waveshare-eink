import importlib
from PIL import Image,ImageDraw,ImageFont

class DisplayManager():

    def __init__(self, screen='epd7in5_V2'):
        epd_factory = importlib.import_module(f'waveshare_epd.{screen}')
        epd = epd_factory.EPD()
        epd.init()
        epd.Clear()

        self.__epd = epd

    def render_image(self, img_path, clear_first=True):
        if clear_first:
            self.__epd.Clear()
        image = Image.open(img_path)
        self.__epd.display(self.__epd.getbuffer(image))

    @property
    def width(self):
        return self.__epd.width

    @property
    def height(self):
        return self.__epd.height