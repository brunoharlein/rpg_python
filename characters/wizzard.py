from .character import Character

class Wizzard(Character):
    """Class representing a wizzard character.
    Attributs: mana
    methods = heal, str"""
    actions: Character.actions.update({'s': 'se soigner'})

    def __init__(self, name = False):
        super().__init__(600, 20, 50, 25, name)
        # Represents the magical power
        self.mana = 200

