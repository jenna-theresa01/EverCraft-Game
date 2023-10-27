from enum import Enum

# class Abilities(Enum):
#     STRENGTH = 10
#     DEXTERITY = 10
#     CONSTITUTION = 10
#     WISDOM = 10
#     INTELLIGENCE = 10
#     CHARISMA = 10

class Mods(Enum):
    ROLL_1 = -5
    ROLL_2 = -4
    ROLL_3 = -4
    ROLL_4 = -3
    ROLL_5 = -3
    ROLL_6 = -2
    ROLL_7 = -2    
    ROLL_8 = -1
    ROLL_9 = -1
    ROLL_10 = 0
    ROLL_11 = 0
    ROLL_12 = 1
    ROLL_13 = 1
    ROLL_14 = 2
    ROLL_15 = 2
    ROLL_16 = 3
    ROLL_17 = 3
    ROLL_18 = 4
    ROLL_19 = 4
    ROLL_20 = 5


    

    # def __init__(self, abilities):
    #     self.abilities = abilities
    #     self._score = 10
    #     self._mod = 0

    # def get_score(self):
    #     return self._score

    # def get_mod(self):
    #     return self._mod

    # def set_score(self, v):
    #     self._score = v
    #     self._mod = self.mods(v)
    
    # score = property(get_score, set_score)

    # mod = property(get_mod)

    # def mod_values(self, score):
    #     mods = {
    #     1: -5,
    #     2: -4,
    #     3: -4,
    #     4: -3,
    #     5: -3,
    #     6: -2,
    #     7: -2,
    #     8: -1,
    #     9: -1,
    #     10: 0,
    #     11: 0,
    #     12: 1,
    #     13: 1,
    #     14: 2,
    #     15: 2,
    #     16: 3,
    #     17: 3,
    #     18: 4,
    #     19: 4,
    #     20: 5
    #     }
    #     self.value = mods.get(score)