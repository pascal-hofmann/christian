"""Some eastereggs just for fun"""

from utils import Filehandler

class EasterEggFunctions(object):
    """Easter Egg functions"""

    def __init__(self):
        self.fhandler = Filehandler()

    def darkwing(self, channel, callback, **kwargs):
        """Post a random line"""
        filename = "./mylines/darkwing.txt"
        myline = self.fhandler.getrandomline(filename)
        callback.say(channel, myline)

    def balu(self, channel, callback, **kwargs):
        """Post a random line"""
        filename = "./mylines/balu.txt"
        myline = self.fhandler.getrandomline(filename)
        callback.say(channel, myline)

    def raspel(self, channel, callback, **kwargs):
        """Post url to raspel"""
        filename = "./myurls/raspel.url"
        url = self.fhandler.getcontent(filename)
        callback.say(channel, url)


