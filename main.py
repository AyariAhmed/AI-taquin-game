from algo.bfs import BFS
from algo.dfs import DFS
from algo.dfs_iterative import DFSIterative
from algo.a_start import AStar1,AStar2
 
if __name__ == '__main__':
    print('\n------- Welcome to tquin game -------\n')
    initial_state = [3, 1, 2, 4, 5, 0, 6, 7, 8]
    user_input = ''
    while user_input != 'q':

        user_input = ''
        while user_input not in ['1','2','3','4','5','q']:
            print(' 1) BFS')
            print(' 2) DFS')
            print(' 3) DFS iterative')
            print(' 4) A* with h1')
            print(' 5) A* with h2')
            print('type q to exit')
            user_input = input('\n-> make a choice: ')
            
        if user_input == '1':
            BFS(initial_state[:])
            print('------------------------------\n')
        elif user_input == '2':
            DFS(initial_state[:])
            print('------------------------------\n')
        elif user_input == '3':    
            DFSIterative(initial_state[:])
            print('------------------------------\n')
        elif user_input == '4':    
            AStar1(initial_state[:])
            print('------------------------------\n')
        elif user_input == '5':    
            AStar2(initial_state[:])
            print('------------------------------\n')

    print('\nuntil next visit...')