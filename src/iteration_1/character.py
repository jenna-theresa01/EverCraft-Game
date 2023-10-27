from iteration_1.AbilityEnum import *
from iteration_1.AbilityScores import *


class Char():
    armor_class = 10
    hit_points = 5
    name = ""
    xp = 0
    level = 1
    abilities = {
        "Strength" : 10,
        "Dexterity" : 10,
        "Constitution" : 15,
        "Wisdom" : 10,
        "Intelligence" : 10,
        "Charisma" : 10,
    }
    roll = int()
    attack_status = ""    
    
    # def set_ability_scores(self):
    #     for ability in Abilities:
    #         ability_value = AbilityScore[ability]
    #         self.abilities.append(ability_value)

    def __init__(self, name, align):
        self.name = name
        self.align = align
            
    # def set_ability_scores(self):
    #     for i in Abilities:
    #         ability_value = Abilities[i]
    #         self.abilities.append(ability_value)

    def apply_strength_mod(self, roll):
        strength_value = self.abilities["Strength"]
        mod_value = Modifiers.mods[f"Value_{strength_value}"]
        self.roll += mod_value
        return self.roll

    def apply_dexterity_mod(self):
        dexterity_value = self.abilities["Dexterity"]
        mod_value = Modifiers.mods[f"Value_{dexterity_value}"]
        self.armor_class += mod_value
        return self.armor_class

    def apply_constitution_mod(self):
        constitution_value = self.abilities["Constitution"]
        mod_value = Modifiers.mods[f"Value_{constitution_value}"]
        self.hit_points += mod_value
        return self.hit_points

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


