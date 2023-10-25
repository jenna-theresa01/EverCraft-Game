from iteration_1.character import *

def test_char_name():
    character = Char("calzone")
    assert character.name is not None