class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class BasisState:

    def __init__(self):
        self.black_pawns = [Pos(1, 1), Pos(1, 2)]
        self.white_pawns = [Pos(8, 1), Pos(8, 2)]

    def try_move(self, pos, turn):
        if turn == 'w' and pos in self.white_pawns:


class State:

    def __init__(self):
        self.states = [(1.0, BasisState)]

    def move(self, pos, turn):
        new_states = []
        for weight, state in self.states:
