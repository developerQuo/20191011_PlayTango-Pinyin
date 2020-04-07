from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt

class Tango_block:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class ScreenObject(Tango_block):
    def __init__(self, name, x, y, id, minmax, mp3, blocks=[], blocks_mp3=[], punch=[]):
        super().__init__(name, id)
        self.size = [x, y]
        self.minmax = minmax
        self.mp3 = mp3
        self.blocks = blocks
        self.blocks_mp3 = blocks_mp3
        self.punch = punch

class Mp3Object(Tango_block):
    def __init__(self, name, mp3, mp3_block_list, mp3_block_question=[], mp3_block_answer=[], punch = []):
        self.name = name
        self.mp3 = mp3
        self.mp3_block_list = mp3_block_list
        self.mp3_block_question = mp3_block_question
        self.mp3_block_answer = mp3_block_answer
        self.punch = punch