from queue import PriorityQueue
from utils import new_state,is_valid_move,print_board
from typing import List



def h_function(board_state : List[int]) -> int:
    '''
    heuristic function returns the number of nodes not in the right place
    '''
    etatFinal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    s = 0
    for i,val in enumerate(board_state) :
        if val == 0:
            continue
        if val != etatFinal[i]:
            s += 1
    return s



def AStar(etatInitial):
    possible_moves = PriorityQueue()
    possible_moves.put((h_function(etatInitial), ""))
    path = ""
    board_state = etatInitial
    count = 0
    while not board_state == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        path = possible_moves.get() # tuple of the node and h_func(node)
        board_state = new_state(etatInitial, path[1])
        count+= 1
        if board_state == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for move in ["L", "R", "U", "D"]:
            acc_moves = path[1] + move
            if is_valid_move(board_state.index(0), move):
                possible_moves.put((h_function(new_state(etatInitial, acc_moves))+len(acc_moves)-1, acc_moves))
    print_board(etatInitial, path[1])

    print(f'- number of visited nodes = {count}')
    print(f'- path length = {len(path)}')