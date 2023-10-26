from enum import Enum

class Abilities(Enum):
    STRENGTH = 1
    DEXTERITY = 2
    CONSTITUTION = 3
    WISDOM = 4
    INTELLIGENCE = 5
    CHARISMA = 6

    def __init__(self, abilities):
        self.abilities = abilities
        self._score = 10
        self._mod = 0

    def get_score(self):
        return self._score

    def get_mod(self):
        return self._mod

    def set_score(self, v):
        self._score = v
        self._mod = self.switcher(v)
    
    score = property(get_score, set_score)

    mod = property(get_mod)

    def mod_values(self, score):
        mods = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5
        }
        return mods.get(score)