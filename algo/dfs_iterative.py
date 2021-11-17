### Author : AyariAhmed
from queue import LifoQueue
from utils import new_state,is_valid_move,print_board
from typing import List


def DFSLimited(etatInitial: List[int],depth : int) -> bool:
    result = False # useful for DFSIterative
    closed_list : List[str] = list() # already checked states
    possibles_moves = LifoQueue()
    possibles_moves.put("")
    path = ""
    board_state = etatInitial
    count = 0
    while not board_state == [1, 2, 3, 4, 5, 6, 7, 8, 0] and not possibles_moves.empty():
        path = possibles_moves.get()
        board_state = new_state(etatInitial, path)
        count += 1
        closed_list.append(board_state)
        # [0, 1, 2, 3, 4, 5, 6, 7, 8] is a possible final state too
        if  board_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for move in ["L", "R", "U", "D"]:
            explore = path + move
            if is_valid_move(board_state.index(0), move) and new_state(etatInitial, explore) not in closed_list and len(explore) <= depth:
                possibles_moves.put(explore)

    if(board_state == [1, 2, 3, 4, 5, 6, 7, 8, 0] or board_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]):
        print_board(etatInitial, path)
        result = True # useful for DFSIterative
    else:
        print(" -- no solution found -- ")
        result = False # useful for DFSIterative
    print(f'- number of visited nodes = {count}')
    print(f'- path length = {len(path)}')
    return result

def DFSIterative(etatInitial: List[int]):
    i = 1
    limit = 25
    while not DFSLimited(etatInitial[:],i):
        print(f' ((((  i = {i}  )))) ')
        print('\n ************************** \n')
        i+=1
        if i == limit:
            break
    if i == limit:
        print(f' =====> no solution was found with depth less than {limit}')
    else :
        print(f'\n =====> solution found with depth {i}')    