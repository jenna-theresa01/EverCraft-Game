import pytest
from iteration_1.character import *
from iteration_2.character2 import *

def test_assign_and_apply_fighter_roll():
    justin = Char("Justin", "Evil", "Fighter")
    justin.roll = 13
    justin.assign_and_apply_fighter()
    assert justin.roll == 14

def test_fighter_hit_points():
    justin = Char("Justin", "Evil", "Fighter")
    justin.assign_and_apply_fighter()
    assert justin.hit_points == 10

def test_monk_hit_points():
    justin = Char("Justin", "Evil", "Monk")
    justin.assign_and_apply_monk()
    assert justin.hit_points == 6

def test_monk_armor_class():
    justin = Char("Justin", "Evil", "Monk")
    justin.assign_and_apply_monk()
    assert justin.armor_class == 10

def test_rogue_dexterity():
    justin = Char("Justin", "Evil", "Rogue")
    justin.roll = 13
    justin.assign_and_apply_rogue()
    assert justin.roll == 13

