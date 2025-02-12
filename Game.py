from TurnOrderEnum import TurnOrderEnum
from Player import Player
from Deck import Deck
from InputSystem import InputSystem
from CardsEnum import CardsEnum


class Game():
    def __init__(self, players):
        self.turn_order = TurnOrderEnum.initialise_game
        #self.no_of_players = self._no_of_players(no_of_players)
        #self.players = [Player(f"Player{i}") for i in range(0, self.no_of_players)]
        self.players = players
        self.deck = Deck(self.no_of_players)
        self.input_system = InputSystem()

        self._give_initial_defuse()
        self._deal_cards()
        self.deck._shuffle_deck()

        self.turn_order = TurnOrderEnum.choose_next_player
        self.next_player_index = -1
        self.is_attacking = False
        self.under_attack = False
        
        self.cards_being_played = []
        self.cards_played_last_turn = []

    def _no_of_players(self, no_of_players):
        if no_of_players > 1 and no_of_players <= 5:
            return no_of_players
        print("Error in number of players")
        return 2

    def _give_initial_defuse(self):
        for player in self.players:
            self.deck.give_initial_defuse(player)

    def _deal_cards(self):
        for _ in range(7):
            for player in self.players:
                player.draw(self.deck.draw_card())

    def _next_player(self):
        #reset the card trackers
        self.cards_played_last_turn = self.cards_being_played 
        self.cards_being_played = []
        
        if self.under_attack and (not self.is_attacking):
            self.under_attack = False
            return self.next_player_index % self.no_of_players

        if self.is_attacking:
            self.under_attack = True
            self.is_attacking = False

        self.next_player_index += 1
        while not self.players[self.next_player_index].is_alive:
            self.next_player_index += 1
            self.next_player_index = self.next_player_index % self.no_of_players
        return self.next_player_index % self.no_of_players

    def game_loop(self):
        while True:
            if self.turn_order == TurnOrderEnum.choose_next_player:
                self.next_player_index = self._next_player()
                self.turn_order = TurnOrderEnum.play_actions

            if self.turn_order == TurnOrderEnum.play_actions:
                self._play_actions()

    def _play_actions(self):
        while self.turn_order == TurnOrderEnum.play_actions:
            current_player = self.players[self.next_player_index]
            print(f"it is {current_player}'s turn")

            card_to_play = self.input_system.pick_action(
                current_player)

            self.cards_being_played += [card_to_play]

            # check if card_to_play is valid
            match card_to_play:
                case -1:  # no action
                    exploding_kitten_position = current_player.draw(self.deck.draw_card(), self.deck)

                    if exploding_kitten_position == 1:
                        exploding_kitten_position = self.input_system.put_back_exploding_kitten(self.deck.deck)
                        self.deck._place_exploding_kitten(exploding_kitten_position)
                    elif exploding_kitten_position == -2:
                        current_player = False
                        count = 0
                        for i in self.players:
                            if i != False:
                                count += 1
                        if count <= 1:
                            print("Game has ended.")
                    self.turn_order = TurnOrderEnum.choose_next_player
                    break

                case 3:
                    print(f"{current_player} used attack!")
                    current_player.use_card(CardsEnum.attack)
                    if self._nope:
                        break
                    self.is_attacking = True
                    self.turn_order = TurnOrderEnum.choose_next_player
                    break

                case 4:
                    print(f"{current_player} used skip")
                    self.players[self.next_player_index].use_card(CardsEnum.skip)

                    if self._nope():
                        break
                    self.turn_order = TurnOrderEnum.choose_next_player
                    break
                
                case 5:
                    self.players[self.next_player_index].use_card(CardsEnum.favor)
                    target_player = self.input_system.pick_target(self.players)
                    print(f"{current_player} used favor on {target_player}")
                    
                    if self._nope():
                        break
                    card_to_give = self.input_system.card_to_give(target_player.hand)
                    self.deck.favor(current_player, target_player, card_to_give)
                    break
                    
                case 6:
                    print(f"{current_player} used shuffle")
                    self.players[self.next_player_index].use_card(CardsEnum.shuffle)
                    if self._nope():
                        break
                    self.deck.shuffle()
                    break
        
                case 7:
                    print(f"{current_player} used see the future")
                    self.players[self.next_player_index].use_card(CardsEnum.see_the_future)
                    if self._nope():
                        break
                    self.deck.see_the_future(current_player)
                    break
                
                case _:
                    if (card_to_play < 12*2):
                        target_player = self.input_system.pick_target(self.players)
                        print(f"{current_player} used steal on {target_player}")
                        
                        if self._nope:
                            break
                        self.deck.steal(card_to_play, current_player, target_player)
                    else:
                        target_player = self.input_system.pick_target(self.players)
                        card_to_steal = CardsEnum(self.input_system.card_to_steal())
                        print(f"{current_player} steals {card_to_steal} from {target_player}")
                        
                        if self._nope:
                            break
                        self.deck.steal_specific(card_to_play, card_to_steal, current_player, target_player)
                    break

    def _nope(self):
        for i in self.players:
            if not i == self.players[self.next_player_index]:
                for j in i.hand:
                    if j == CardsEnum.nope:
                        nope = int(
                            input(f"Does {i} want to nope?\n"))
                        if nope == 1:
                            i.use_card(CardsEnum.nope)
                            return True
                        
if __name__ == "__main__":
    a = GameManager()
    a.game_loop()
