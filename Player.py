from CardsEnum import CardsEnum
import random


class Player():
    def __init__(self, name):
        self.name = str(name)
        self.hand = []
        self.hand_size = 0
        self.is_alive = True

    def valid_actions(self):
        action_hand = self.hand

        is_removing = True
        while is_removing:
            try:
                action_hand.remove(CardsEnum.defuse)
            except:
                is_removing = False
        is_removing = True
        while is_removing:
            try:
                action_hand.remove(CardsEnum.nope)
            except:
                is_removing = False

        counters = [0, 0, 0, 0, 0]
        for card in self.hand:
            if card.value >= 8 and card.value <= 12:
                counters[card.value - 8] += 1
                action_hand.remove(card)

        no_of_pairs = [0, 0, 0, 0, 0]
        no_of_trios = [0, 0, 0, 0, 0]
        for i in counters:
            no_of_pairs[i] = counters[i] % 2
            no_of_trios[i] = counters[i] % 3

        self._action_hand_helper(
            action_hand, no_of_pairs[0], CardsEnum.pair_taco_cat)
        self._action_hand_helper(
            action_hand, no_of_pairs[1], CardsEnum.pair_cattermelon)
        self._action_hand_helper(
            action_hand, no_of_pairs[2], CardsEnum.pair_hairy_patato_cat)
        self._action_hand_helper(
            action_hand, no_of_pairs[3], CardsEnum.pair_beard_cat)
        self._action_hand_helper(
            action_hand, no_of_pairs[4], CardsEnum.pair_rainbow_ralphing_cat)

        self._action_hand_helper(
            action_hand, no_of_trios[0], CardsEnum.pair_taco_cat)
        self._action_hand_helper(
            action_hand, no_of_trios[1], CardsEnum.pair_cattermelon)
        self._action_hand_helper(
            action_hand, no_of_trios[2], CardsEnum.pair_hairy_patato_cat)
        self._action_hand_helper(
            action_hand, no_of_trios[3], CardsEnum.pair_beard_cat)
        self._action_hand_helper(
            action_hand, no_of_trios[4], CardsEnum.pair_rainbow_ralphing_cat)

    def _action_hand_helper(self, action_hand, number_of, card_type):
        while number_of > 0:
            action_hand.append(card_type)
            number_of -= 1

    def draw(self, card):
        if card == CardsEnum.exploding_kitten:
            if CardsEnum.defuse in self.hand:
                self.hand.remove(CardsEnum.defuse)
                return int(input("Where to put exploding kitten?"))
            else:
                print("Player died")
                self.is_alive = False
                return -2

        self.hand += [card]
        self.hand_size += 1
        return -1

    def give_card(self):
        card_to_give = input(f"Choose which card to give:\n{self.hand}.")
        # check if valid
        card_to_give = int(card_to_give)
        card_to_give = Deck(card_to_give)
        self.hand.remove(card_to_give)
        return card_to_give

    def give_random(self):
        random_num = random.randint(0, self.hand_size-1)
        card = self.hand[random_num]
        self.hand.remove(card)
        return card

    def use_card(self, card):
        self.hand.remove(card)

    def __str__(self):
        string = self.name + " has the cards: [ "
        for i in range(0, self.hand_size - 1):
            string += str(self.hand[i]) + " , "
        string += str(self.hand[self.hand_size - 1]) + " ]"
        return string
