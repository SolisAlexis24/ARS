"""
    1: es una pared
    0: camino libre
    S: comienzo
    M: meta
"""
import os
#Maze_solver class to identify where is the program currently

class Maze_solver():
    def __init__(self, maze) -> None:
        # Inicialización de los atributos (Varaibles)
        self.x = None #x coordinate of the Maze_solver
        self.y = None   #y coordinate of the Maze_solver
        self.maze = maze #maze to solve
        self.orientation = None #Orientation of the maze solver
        self.find_start()
        if self.x is None:
            exit(1)
        self.forward_x = self.x + 1 # 1  x coordinate of the front of the maze solver (where it is facing at)
        self.forward_y = self.y  # 0  y coordinate of the front of the maze solver (where it is facing at)
        self.def_orientation() #Defining the orientation of the maze solver
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0

    # Método para imprimir el laberinto y la información
    def show(self) -> None:
        """Method to print the coordinates of the Maze_solver"""
        for i in range(self.rows):
            for j in range(self.cols):
                if i == self.x and j == self.y:
                    print('\t[X]', end='')
                else:
                    print(f'\t{self.maze[i][j]}', end='')
            print('\n')
        print(f'\t\t\t    Posición actual: ( {self.x}, {self.y} )')
        print(f'\t\t\t\tMirando a: ( {self.forward_x}, {self.forward_y} )')
        print()

    # Verifica si no las coordenadas no se salen del laberinto
    def exists(self, x: int, y: int) -> bool:
        """Method to check if the provided coordinates exists
        :param x: Row
        :param y: Column
        :return: True if the coordinates are valid"""
        return 0 <= x < self.rows and 0 <= y < self.cols

    # This method was created in order to go ahead or turn back
    # S y W avanza
    # Antihorario
    def turnCC(self) -> None:
        """Method to turn one pixel counterclockwise the front of the maze solver"""
        #If the mz is looking South -> Look East
        if self.orientation == 'S':
            self.forward_x = self.x
            self.forward_y = self.y + 1
            self.orientation = 'E'
        #If the mz is looking West -> Look South
        elif self.orientation == 'W': # Oeste
            self.forward_x = self.x + 1
            self.forward_y = self.y
            self.orientation = 'S'
        #If the mz is looking North -> Look West
        elif self.orientation == 'N':
            self.forward_x = self.x
            self.forward_y = self.y - 1
            self.orientation = 'W'
        #If the mz is looking East -> Look North
        elif self.orientation == 'E':
            self.forward_x = self.x - 1
            self.forward_y = self.y
            self.orientation = 'N'

    # Horario
    def turnC(self) -> None:
        """Method to turn one pixel clockwise the front of the maze solver"""
        #If the mz is looking South -> Look West
        if self.orientation == 'S':
            self.forward_x = self.x
            self.forward_y = self.y - 1
            self.orientation = 'W'
        #If the mz is looking West -> Look North
        elif self.orientation == 'W':
            self.forward_x = self.x - 1
            self.forward_y = self.y
            self.orientation = 'N'
        #If the mz is looking North -> Look East
        elif self.orientation == 'N':
            self.forward_x = self.x
            self.forward_y = self.y + 1
            self.orientation = 'E'
        #If the mz is looking East -> Look South
        elif self.orientation == 'E':
            self.forward_x = self.x + 1
            self.forward_y = self.y
            self.orientation = 'S'

    def def_orientation(self):
        """Method to define the maze solver orientation (Noth (N), South (S), East (E) or Weast (W))"""
        #If the mz is looking South
        if self.forward_x > self.x and self.forward_y == self.y:
            self.orientation = 'S'
        #If the mz is looking West
        elif self.forward_x == self.x and self.forward_y < self.y:
            self.orientation = 'W'
        #If the mz is looking North
        elif self.forward_x < self.x and self.forward_y == self.y:
            self.orientation = 'N'
        #If the mz is looking East
        elif self.forward_x == self.x and self.forward_y > self.y:
            self.orientation = 'E'

    def go_ahead(self):
        """Method to make the maze solver move one square towards the position it is looking at"""
        #If the mz is looking South
        if self.orientation == 'S':
            self.x = self.forward_x
            self.forward_x += 1
        #If the mz is looking West
        elif self.orientation == 'W':
            self.y = self.forward_y
            self.forward_y -= 1
        #If the mz is looking North
        elif self.orientation == 'N':
            self.x = self.forward_x
            self.forward_x -= 1
        #If the mz is looking East
        elif self.orientation == 'E':
            self.y = self.forward_y
            self.forward_y += 1

    def solve_sra(self, n: int) -> None:
        """Method to solve the maze with the Simple Reflex Agent algorithm
        :param n: Number of movements that the maze solver can do, it includes turning and go ahead
        """
        # The code repeats itself n times
        for _ in range(n):
            print(f'\n\t\t=============== Iteration {_} ===============')
            self.show()
            # #################################################################
            #If the coordinate of the towards square from the maze is valid
            if self.exists(self.forward_x, self.forward_y):
                #get the symbol of the square towards
                # front symbol (x,y)
                front_symbol = self.maze[self.forward_x][self.forward_y]
                # =================================================== 
                #if the maze solver can move into the towards square according to the rules
                if front_symbol == 0 or front_symbol == 'S' or front_symbol == 'M':
                    self.go_ahead()
                    #If the current location symbol is the goal
                    if self.maze[self.x][self.y] == 'M':
                        print("\n\n\t\t==-==-==-==-==-== M E T A ==-==-==-==-==-==")
                        self.show()
                        print('LLEGASTE A LA METAAAAAA AAAA TE AMO DEEEYYYY')
                        exit(0)
                else:
                    self.turnCC()
                # =================================================== 
            else:
                self.turnCC()
             # ############################################################### 
        print("Goal not found!!!")


    def find_start(self):
        """Find the coordinates of the goal 'S' in the maze"""
        for i in range(len(self.maze)):           # Recorre las filas
            for j in range(len(self.maze[i])):    # Recorre las columnas
                if self.maze[i][j] == 'S':        # Si encuentra el inicio
                    self.x = i
                    self.y = j
                    break

ex1 = [[0, 0, 0, 0, 0, 0, 0, 0, 'S'],
       [0, 1, 1, 0, 0, 1, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 'M', 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 1, 1, 0, 0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]
       ]

if __name__ == "__main__":
    os.system('cls')
    mz = Maze_solver(ex1)
    # Numero de intentos
    mz.solve_ars(100)
