from enum import Enum


class TurnOrder(Enum):
    initialise_game = 0
    choose_next_player = 1
    play_actions = 2
    draw = 3
    end_game = 4
