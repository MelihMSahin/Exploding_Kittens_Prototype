class Player():
    def __init__(self, name):
        self.name = str(name)
        self.hand = []
        self.hand_size = 0

    def add_card(self, card):
        self.hand += [card]
        self.hand_size += 1

    def __str__(self):
        string = self.name + " has the cards: [ "
        for i in range(0, self.hand_size - 1):
            string += str(self.hand[i]) + " , "
        string += str(self.hand[self.hand_size - 1]) + " ]"
        return string
