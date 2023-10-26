import pytest
from iteration_1.character import *
from iteration_1.AbilityEnum import *
from iteration_1.AbilityScores import *

def test_char_name():
    character = Char("Justin", "Evil")
    assert character.name is not None


def test_char_align():
    character = Char("Justin", "Evil")
    assert character.align is not None


def test_armor_class():
    character = Char("Justin", "Evil")
    assert character.armor_class == 10


def test_hit_points():
    character = Char("Justin", "Evil")
    assert character.hit_points == 5


def test_declare_attack():
    roll = 18
    defender = Char("Justin", "Evil")
    assert roll >= defender.armor_class

def test_get_hurt():
    justin = Char("Justin", "Evil")
    tanner = Char("Tanner", "Good")
    justin.declare_attack(tanner, 18)
    assert tanner.hit_points == 4

def test_abilities_exists():
    justin = Char("Justin", "Evil", "Strength")
    assert justin.abilities is not None

# def test_ability_modifier():
#     assert Skill_Mods ; 1 == -5


def test_xp_gain():
    justin = Char("Justin", "Evil")
    justin.xp_gain(10)
    assert justin.xp == 10

def test_gain_level():
    justin = Char("Justin", "Evil")
    justin.xp_gain(990)
    justin.xp_gain(10)
    print(justin.xp)
    justin.gain_level()
    assert justin.level == 2

