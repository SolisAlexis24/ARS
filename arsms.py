

#Maze_solver class to identify where is the program currently

class Maze_solver():
    def __init__(self) -> None:
        self.x = 0 #x coordinate of the Maze_solver
        self.y = 0 #y coordinate of the Maze_solver
    
    def show(self) ->None:
        '''Method to print the coordinates of the maze_solver'''
        print(f'maze_solver at ( {self.x}, {self.y} )')

    def solve(self, maze) ->None:
        ...








