from iteration_1.AbilityEnum import *
from iteration_1.AbilityScores import *


class Char():
    armor_class = 10
    hit_points = 5
    xp = 0
    level = 1
    abilities = {
        "Strength" : 10,
        "Dexterity" : 10,
        "Constitution" : 10,
        "Wisdom" : 10,
        "Intelligence" : 10,
        "Charisma" : 10,
    }
    roll = int()  

    def __init__(self, name, align, customize):
        self.name = name
        self.align = align
        self.customize = customize

    def assign_and_apply_fighter(self):
        if self.customize is "Fighter":
            roll_mod = (1 * self.level)
            self.roll += roll_mod
            hitpoints_mod = (10 * self.level)
            self.hit_points = hitpoints_mod
            return self.roll, self.hit_points
            
    def assign_and_apply_monk(self):
        if self.customize is "Monk":
            hitpoints_mod = (6 * self.level)
            self.hit_points = hitpoints_mod
            wisdom_value = self.abilities["Wisdom"]
            mod_value = Modifiers.mods[f"Value_{wisdom_value}"]
            if mod_value >= 0:
                self.armor_class += mod_value
            return self.hit_points, self.armor_class

    def assign_and_apply_rogue(self):
        if self.customize is "Rogue":
            dexterity_value = self.abilities["Dexterity"]
            mod_value = Modifiers.mods[f"Value_{dexterity_value}"]
            self.roll += mod_value
            if self.attack_status == "crit":
                self.damage *= 3
            return self.roll, self.damage

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


