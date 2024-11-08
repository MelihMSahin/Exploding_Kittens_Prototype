from enum import Enum


class Deck(Enum):
    defuse = 0
    nope = 1
    exploding_kitten = 2
    attack = 3
    skip = 4
    favor = 5
    shuffle = 6
    see_the_future = 7
    taco_cat = 9
    cattermelon = 10
    hairy_patato_cat = 11
    beard_cat = 12
    rainbow_ralphing_cat = 13

    def __str__(self):
        return self.name
