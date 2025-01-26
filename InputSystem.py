from Player import Player


class InputSystem:
    def __init__(self):
        pass

    def pick_action(self, player):
        valid_actions = []

        return int(input(
            f"Choose which action to play: {self.players[self.next_player_index].hand}.\n"))
