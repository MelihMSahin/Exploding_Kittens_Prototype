import random
import queue
from Deck import Deck
from Player import Player
from TurnOrder import TurnOrder


class GameMaster():
    def __init__(self):
        self.turn_order = TurnOrder.initialise_game
        self.deck = self._make_deck()
        self._shuffle_deck()
        self.no_of_players = 2  # self._no_of_players()
        self.players = [Player(i) for i in range(0, self.no_of_players)]
        self._give_initial_defuse()
        self._deal_cards()
        self._add_defuses_and_exploding_kittens()
        self.turn_order = TurnOrder.choose_next_player

    def _no_of_players(self):
        no_of_players = input("How many people are playing?\n ")
        while True:
            try:
                no_of_players = int(no_of_players)
                if (no_of_players > 1 and no_of_players < 6):
                    break
            except:
                pass
            no_of_players = input("Please enter a number between 2 and 5.\n")
        return no_of_players

    def _make_deck(self):
        deck = queue.Queue()
        for _ in range(5):
            deck.put(Deck.nope)
        for _ in range(4):
            deck.put(Deck.attack)
        for _ in range(4):
            deck.put(Deck.skip)
        for _ in range(4):
            deck.put(Deck.favor)
        for _ in range(4):
            deck.put(Deck.shuffle)
        for _ in range(5):
            deck.put(Deck.see_the_future)
        for _ in range(4):
            deck.put(Deck.taco_cat)
        for _ in range(4):
            deck.put(Deck.cattermelon)
        for _ in range(4):
            deck.put(Deck.hairy_patato_cat)
        for _ in range(4):
            deck.put(Deck.beard_cat)
        for _ in range(4):
            deck.put(Deck.rainbow_ralphing_cat)
        return deck

    def _shuffle_deck(self):
        temp_arr = [None for _ in range(self.deck.qsize())]
        for i in range(len(temp_arr)):
            temp_arr[i] = self.deck.get()
        random.shuffle(temp_arr)
        for i in range(len(temp_arr)):
            self.deck.put(temp_arr[i])

    def _give_initial_defuse(self):
        for player in self.players:
            player.add_card(Deck.defuse)

    def _deal_cards(self):
        for _ in range(7):
            for player in self.players:
                player.add_card(self.draw_card())

    def draw_card(self):
        return self.deck.get()

    def _add_defuses_and_exploding_kittens(self):
        for _ in range(0, 6 - self.no_of_players):
            self.deck.put(Deck.defuse)
        for _ in range(0, self.no_of_players - 1):
            self.deck.put(Deck.exploding_kitten)
        self._shuffle_deck()

    def __str__(self):
        string = "[ "
        temp_arr = [None for _ in range(self.deck.qsize())]
        for i in range(len(temp_arr)):
            temp_arr[i] = self.deck.get()
        for i in range(len(temp_arr)):
            string += str(temp_arr[i]) + " "
            self.deck.put(temp_arr[i])
        return string + "]"


if __name__ == "__main__":
    gm = GameMaster()
    print(gm)
