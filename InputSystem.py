from Player import Player


class InputSystem:
    def __init__(self):
        pass

    def pick_action(self, player):
        valid_actions = player.valid_actions()

        action = int(input(f"Choose which action to play: {valid_actions}.\n"))

        return valid_actions[action].value
    
    def pick_target(self, players):
        valid_targets = [0 for i in range(len(players))]
        str = "Pick a target from: "
        for i in range(len(players)):
            if players[i].is_alive:
                str += f" {i} for {players[i]},"
                valid_targets[i] = 1
                
        target_no = int(input(f"{str}"))
        while (valid_targets[target_no] == 0):
            target_no = int(input(f"{str}"))
            
        return players[target_no]
    
    def card_to_steal(self):
        card_no = int(input("Pick card to steal from 0 to 12:"))
        while (card_no > 12 or card_no < 0 or card_no == 2):
            card_no = int(input("Pick a valid number betwen 0 and 12 but not 2"))
        return card_no
    
    def put_back_exploding_kitten(self, deck):
        position = int(input("Where to put exploding kitten?"))
        while position < len(deck.deck):
            position = int(input("Where to put exploding kitten?"))
        return position
    
    def card_to_give(self, hand):
        return input(f"Choose which card to give:\n{hand}.")
        
