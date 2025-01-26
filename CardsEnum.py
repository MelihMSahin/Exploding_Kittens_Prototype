from enum import Enum


class CardsEnum(Enum):
    defuse = 0
    nope = 1
    exploding_kitten = 2
    attack = 3
    skip = 4
    favor = 5
    shuffle = 6
    see_the_future = 7
    taco_cat = 8
    cattermelon = 9
    hairy_patato_cat = 10
    beard_cat = 11
    rainbow_ralphing_cat = 12

    # pairs and trios
    pair_taco_cat = 8*2
    pair_cattermelon = 9*2
    pair_hairy_patato_cat = 10*2
    pair_beard_cat = 11*2
    pair_rainbow_ralphing_cat = 12*2

    trio_taco_cat = 8*3
    trio_cattermelon = 9*3
    trio_hairy_patato_cat = 10*3
    trio_beard_cat = 11*3
    trio_rainbow_ralphing_cat = 12*3

    def __str__(self):
        return self.name


if __name__ == "__main__":
    print(CardsEnum.value.__get__())
