import random
from CardsEnum import CardsEnum
from Player import Player


class Deck():
    def __init__(self, no_of_players):
        self.deck = self._make_deck()
        self.no_of_players = no_of_players
        self._shuffle_deck()

    def give_initial_defuse(self, player):
        player.draw(CardsEnum.defuse)

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

    def favor(self, player, target_player, card):
        player.draw(target_player.give_card())

    def shuffle(self):
        self._shuffle_deck()

    def see_the_future(self, player):
        print(f"The next three cards are {self.deck[0]}, {self.deck[1]} and {self.deck[2]}")

    def steal(self, card_no, player, target_player):
        card_no = card_no/2;
        player.use_card(CardsEnum(card_no))
        player.use_card(CardsEnum(card_no))
        player.draw(target_player.give_random())
        
    def steal_specific(self, card_played, card_to_steal, player, target_player):
        card_played = card_played/3;
        player.use_card(CardsEnum(card_played))
        player.use_card(CardsEnum(card_played))
        player.use_card(CardsEnum(card_played))
        if target_player.give(card_to_steal) is not None:
            player.draw(card_to_steal)

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
