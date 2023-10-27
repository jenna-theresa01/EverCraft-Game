from enum import Enum

from iteration_1.AbilityEnum import *
from iteration_1.AbilityScores import *

class Attribute(Enum):
    """Enum for character attributes."""
    STRENGTH = "Strength"
    DEXTERITY = "Dexterity"
    CONSTITUTION = "Constitution"
    INTELLIGENCE = "Intelligence"
    WISDOM = "Wisdom"
    CHARISMA = "Charisma"


class Char():
    """Class for character attributes and methods."""
    armor_class = 10
    hit_points = 5
    name = ""
    xp = 0
    level = 1
    abilities = []


    attack_status = ""    

    def __init__(self, name, align):
        self.name = name
        self.align = align
        self.attributes = {
            Attribute.STRENGTH: 10,
            Attribute.DEXTERITY: 10,
            Attribute.CONSTITUTION: 10,
            Attribute.INTELLIGENCE: 10,
            Attribute.WISDOM: 10,
            Attribute.CHARISMA: 10,
        }
    

    def set_attribute(self, attribute: Attribute, value: int):
        if type(attribute) != Attribute:
            raise TypeError("attribute must be an instance of Attribute Enum")
        self.attributes[attribute] = value

    def set_mods(self, attribute: Attribute, roll: int):
        if type(attribute) != Attribute:
            raise TypeError("attribute must be an instance of Attribute Enum")
        
        # Figure out the modifier and then add it to the attribute's current value
        self.set_attribute[attribute] = self.attributes[attribute].value + [f"ROLL_{roll}"].value
        


    # self.set_ability_scores()
            
    # def set_ability_scores(self):
    #     for i in Abilities:
    #         ability_value = Abilities[i]
    #         self.abilities.append(ability_value)

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


