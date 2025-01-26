import random
from CardsEnum import CardsEnum
from Player import Player


class Deck():
    def __init__(self, no_of_players):
        self.deck = self._make_deck()
        self.no_of_players = no_of_players
        self._shuffle()

    def give_initial_defuse(self, player):
        player.draw_card(CardsEnum.defuse)

    def _get(self):
        temp = self.deck[0]
        for i in range(1, len(self.deck)):
            self.deck[i-1] = self.deck[i]
        return temp

    def _make_deck(self):
        deck = []
        for _ in range(5):
            deck += [CardsEnum.nope]
        for _ in range(4):
            deck += [CardsEnum.attack]
        for _ in range(4):
            deck += [CardsEnum.skip]
        for _ in range(4):
            deck += [CardsEnum.favor]
        for _ in range(4):
            deck += [CardsEnum.shuffle]
        for _ in range(5):
            deck += [CardsEnum.see_the_future]
        for _ in range(4):
            deck += [CardsEnum.taco_cat]
        for _ in range(4):
            deck += [CardsEnum.cattermelon]
        for _ in range(4):
            deck += [CardsEnum.hairy_patato_cat]
        for _ in range(4):
            deck += [CardsEnum.beard_cat]
        for _ in range(4):
            deck += [CardsEnum.rainbow_ralphing_cat]
        return deck

    def _shuffle_deck(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self._get()

    def add_defuses_and_exploding_kittens(self):
        for _ in range(0, 6 - self.no_of_players):
            self.deck += [CardsEnum.defuse]
        for _ in range(0, self.no_of_players - 1):
            self.deck += [CardsEnum.exploding_kitten]
        self._shuffle_deck()

    def __str__(self):
        string = "[ "
        for i in self.deck:
            string += i
        return string + "]"

    def _nope(self):
        for i in self.players:
            if not i == self.players[self.next_player_index]:
                for j in i.hand:
                    if j == CardsEnum.nope:
                        nope = int(input("Nope?\n"))
                        if nope == 1:
                            i.use_card(CardsEnum.nope)
                            return True

    def _attack(self):
        print("player used attack")
        self.players[self.next_player_index].use_card(CardsEnum.attack)
        if self._nope():
            return
        self.is_attacking = True
        self.turn_order = TurnOrderEnum.choose_next_player

    def _skip(self):
        print("player used skip")
        self.players[self.next_player_index].use_card(CardsEnum.skip)
        if self._nope():
            return
        self.turn_order = TurnOrderEnum.choose_next_player

    def _favor(self):
        print("player used favor")
        self.players[self.next_player_index].use_card(CardsEnum.favor)
        if self._nope():
            return
        target_player = int(input("Choose a target player:\n"))
        self.players[self.next_player_index].draw(
            self.players[target_player].give_card())

    def _shuffle(self):
        print("player used shuffle")
        self.players[self.next_player_index].use_card(CardsEnum.shuffle)
        if self._nope():
            return
        self._shuffle_deck()

    def _see_the_future(self):
        print("player used see the future")
        self.players[self.next_player_index].use_card(CardsEnum.see_the_future)
        if self._nope():
            return
        print(
            f"The next three cards are {self.deck[0]}, {self.deck[1]} and {self.deck[2]}")

    def _steal(self, card_no):
        print("player used steal")
        self.players[self.next_player_index].use_card(CardsEnum(card_no))
        self.players[self.next_player_index].use_card(CardsEnum(card_no))
        if self._nope():
            return
        target_player = int(input("Choose a target player:\n"))
        self.players[self.next_player_index].draw(
            self.players[target_player].give_random())

    def _place_exploding_kitten(self, position):
        temp = [None for _ in range(len(self.deck) + 1)]
        for i in range(position):
            temp[i] = self._get()
        temp[position] = CardsEnum.exploding_kitten
        for i in range(position + 1, len(self.deck) + 1):
            temp[i] = self._get()
        self.deck = temp


if __name__ == "__main__":
    pass
