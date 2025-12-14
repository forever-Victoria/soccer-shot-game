import random

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.score = 0

    def choose_direction(self, direction):
        return direction.upper()


class Goalkeeper:
    def __init__(self, name="Goalkeeper"):
        self.name = name
        self.saves = 0

    def guess_direction(self):
        return random.choice(["L", "C", "R"])
