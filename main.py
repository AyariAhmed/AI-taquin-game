from algo.bfs import BFS
from algo.dfs import DFS
from algo.dfs_limited import DFSIterative
from algo.a_start import AStar1,AStar2
 
if __name__ == '__main__':
    print('\n------- Welcome to tquin game -------\n')
    user_input = ''
    while user_input != 'q':

        user_input = ''
        while user_input not in ['1','2','3','4','5','q']:
            print(' 1) BFS')
            print(' 2) DFS')
            print(' 3) DFS limited')
            print(' 4) A* with h1')
            print(' 5) A* with h2')
            print('type q to exit')
            user_input = input('\n-> make a choice: ')
            
        if user_input == '1':
            BFS([1, 8, 2, 4, 0, 3, 7, 6, 5])
            print('------------------------------\n')
        elif user_input == '2':
            DFS([4, 1, 2, 7, 5, 3, 8, 6, 0])
            print('------------------------------\n')
        elif user_input == '3':    
            DFSIterative([1, 2, 3, 4, 5, 6, 0, 7, 8])
            print('------------------------------\n')
        elif user_input == '4':    
            AStar1([1, 8, 2, 4, 0, 3, 7, 6, 5])
            print('------------------------------\n')
        elif user_input == '5':    
            AStar2([1, 8, 2, 4, 0, 3, 7, 6, 5])
            print('------------------------------\n')

    print('\nuntil next visit...')