from queue import LifoQueue
from utils import new_state,is_valid_move,print_board
from typing import List

def DFS(etatInitial : List[int]):
    closed_list : List[str] = list() # already checked states
    possibles_moves = LifoQueue()
    possibles_moves.put("")
    path = "" # path to the final state
    board_state = etatInitial
    count = 0
    while not board_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        path : str = possibles_moves.get()
        board_state = new_state(etatInitial, path)
        count+=1
        # mark the board_state as visited in the closed_list list 
        closed_list.append(board_state)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8] is a possible final state
        if  board_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        
        for move in ["D", "R", "U", "L"]:
            explore : str = path + move
            if is_valid_move(board_state.index(0), move) and new_state(etatInitial, explore) not in closed_list:
                possibles_moves.put(explore)

    print_board(etatInitial, path)
    print(f'- number of visited nodes = {count}')
    print(f'- path length = {len(path)}')