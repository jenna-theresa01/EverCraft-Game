class Char:
    armor_class = 10
    hit_points = 5
    name = ""
    xp = 0
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    level = 1

    attack_status = ""    
    
    def __init__(self, name, align):
        self.name = name
        self.align = align
        
    def declare_attack(self, defender, roll):
        if roll >= defender.armor_class:
            self.attack_status = "hit"
            defender.hit_points -= 1
        elif roll == 20:
            self.attack_status = "crit"
            defender.hit_points -= 2
        else: 
            self.attack_status = "miss"

    def xp_gain(self, v):
        self.xp += v
        
    def gain_level(self):
        if self.xp >= 1000:
            levels_gained = self.xp//1000
            self.level += levels_gained
            self.hit_points += levels_gained
            self.xp -= levels_gained * 1000


