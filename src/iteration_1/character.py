class Char:
    armor_class = 10
    hit_points = 5
    name = ""
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    
    
    def __init__(self, name, align):
        self.name = name
        self.align = align
        
    def declare_attack(self, defender, roll):
        if roll >= defender.armor_class:
            defender.hit_points -= 1
        elif roll == 20:
            defender.hit_points -= 2
        

class Skill_Mods:
    {
    1 : -5,
    2 : -4, 
    3 : -4,
    4 : -3,
    5 : -3,
    6 : -2,
    7 : -2,
    8 : -1,
    9 : -1,
    10 : 0,
    11 : 0,
    12 : 1,
    13 : 1,
    14 : 2,
    15 : 2,
    16 : 3,
    17 : 3,
    18 : 4,
    19 : 4,
    20 : 5,
    }
