from enum import Enum


class TurnOrderEnum(Enum):
    initialise_game = 0
    choose_next_player = 1
    play_actions = 2
    draw = 3
    end_game = 4
    wait = 5
