from typing import List
import numpy as np


def print_board(board_state,path):
    '''
    given the board and the path it prints the board from the initial to the final state
    '''
    board_state[board_state.index(0)] = 'X';
    print(np.array(board_state).reshape(3,3),end='\n\n')

    for move in path:
        index = board_state.index('X')
        if move == "L":
            board_state[index] = board_state[index - 1]
            board_state[index - 1] = 'X'
        elif move == "R":
            board_state[index] = board_state[index + 1]
            board_state[index + 1] = 'X'

        elif move == "U":
            board_state[index] = board_state[index - 3]
            board_state[index - 3] = 'X'

        elif move == "D":
            board_state[index] = board_state[index + 3]
            board_state[index + 3] = 'X'

        print(np.array(board_state).reshape(3,3),end='\n\n')

        

def is_valid_move(index_0 : int,move : str) -> bool:
    '''
    Checks if the move is possible 
    '''
    if move == "L":
         # [0,3,6] are the left bounderies of the board
        return index_0 not in [0,3,6]

    elif move == "R":
         # [2,5,8] are the right bounderies of the board
        return index_0 not in [2,5,8]

    elif move == "U":
         # [0,1,2] are the upper bounderies of the board
        return index_0 not in [0,1,2]

    elif move == "D":
         # [6,7,8] are the lower bounderies of the board
        return index_0 not in [6,7,8]



def new_state(etatInitial : List[int],moves : str) -> List[int]:
    '''
    Returns the new state after applying the moves
    '''
    nouv_etat = etatInitial[:]
    for move in moves:
        index = nouv_etat.index(0)

        if move == "L":
            # swap 0 and left node
            nouv_etat[index] = nouv_etat[index - 1]
            nouv_etat[index - 1] = 0

        elif move == "R":
            # swap 0 and right node
            nouv_etat[index] = nouv_etat[index + 1]
            nouv_etat[index + 1] = 0

        elif move == "U":
            # swap 0 and up node
            nouv_etat[index] = nouv_etat[index - 3]
            nouv_etat[index - 3] = 0

        elif move == "D":
            # swap 0 and down node
            nouv_etat[index] = nouv_etat[index + 3]
            nouv_etat[index + 3] = 0

    return nouv_etat