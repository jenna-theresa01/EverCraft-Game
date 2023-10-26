from iteration_1.AbilityEnum import *
from iteration_1.AbilityScores import *


class Char:
    armor_class = 10
    hit_points = 5
    name = ""
    xp = 0
    level = 1
    abilities = []

    attack_status = ""    
    
    def __init__(self, name, align, abilities):
        self.name = name
        self.align = align
        self.abilities = abilities
        self.set_ability_scores()               
                
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


