import pytest
from rich import print, inspect
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

def test_attributes_exists():
    justin = Char("Justin", "Evil")
    assert justin.attributes is not None

def test_attributes_has_default_value():
    justin = Char("Justin", "Evil")
    assert justin.attributes[Attribute.STRENGTH] == 10
    assert justin.attributes[Attribute.DEXTERITY] == 10
    assert justin.attributes[Attribute.CONSTITUTION] == 10
    assert justin.attributes[Attribute.INTELLIGENCE] == 10
    assert justin.attributes[Attribute.WISDOM] == 10
    assert justin.attributes[Attribute.CHARISMA] == 10

def test_attributes_has_default_value_inverse():
    justin = Char("Justin", "Evil")
    with pytest.raises(Exception):
        assert justin.attributes[Attribute.STRENGTH] == 18

def test_set_attribute():
    justin = Char("Justin", "Evil")
    assert justin.attributes[Attribute.STRENGTH] == 10
    justin.set_attribute(Attribute.STRENGTH, 18)
    assert justin.attributes[Attribute.STRENGTH] == 18
    justin.set_attribute(Attribute.DEXTERITY, 15)
    assert justin.attributes[Attribute.DEXTERITY] == 15


# def test_attribute_str_has_default_value():
#     justin = Char("Justin", "Evil")

#     inspect(justin)

#     assert justin.attributes.STRENGTH == 10
#     assert justin.attributes.STRENGTH is not None


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

