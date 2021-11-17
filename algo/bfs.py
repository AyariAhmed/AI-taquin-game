from queue import Queue
from utils import new_state,is_valid_move,print_board
from typing import List

def BFS(etatInitial : List[int]):
    possible_moves = Queue()
    possible_moves.put("")
    path = ""
    board_state = etatInitial
    count = 0
    while not board_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        path = possible_moves.get()
        board_state = new_state(etatInitial, path)
        count=+ 1
        # [0, 1, 2, 3, 4, 5, 6, 7, 8] is a possible final state
        if  board_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for move in ["L", "R", "U", "D"]:
            acc_moves = path + move
            if is_valid_move(board_state.index(0), move):
                possible_moves.put(acc_moves)

    print_board(etatInitial, path)
    print(f'- number of visited nodes = {count}')
    print(f'- path length = {len(path)}')