import random
from bke import *

class Opponent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class AI(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal += 2
        if can_win(board, my_symbol):
            getal += 3
        if is_winner(board, my_symbol):
            getal = 10
        elif can_win(board, opponent_symbol):
            getal = -10
        return getal
    
opponent = Opponent()
ai = AI()

start(player_o=ai, player_x=opponent)