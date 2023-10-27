from enum import Enum, auto, unique


@unique
class Car(Enum):
    FARRARI = 1
    TESLA = 2
    KIA = 3
    TOYOTA = 4
    VOLTSWGON = auto()

class Hero(Enum):
    strength = 10
    agi = 20
    intel = 30


x = Hero

print(x.strength.value)

print(type(x))
print(repr(x))