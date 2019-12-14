from .character import Character

class Warrior(Character):
    """Class representing a warrior character"""
    def __init__(self, name = False):
        super().__init__(500, 50, 80, 10, name)