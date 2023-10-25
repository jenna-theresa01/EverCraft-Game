from iteration_1.character import *

def test_char_name():
    character = Char("potato", "Evil")
    assert character.name is not None


def test_char_align():
    character = Char("potato", "Evil")
    assert character.align is not None


def test_armor_class():
    assert Char.armor_class == 10


def test_hit_points():
    assert Char.hit_points == 5