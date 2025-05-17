"""
Insert your code bellow 

our task is to implement an algorithm that can find the way out of a maze.

The maze representation is like this:

    [
      [1,1,1,1,1],
      [1,0,0,1,1],
      [1,1,0,1,1],
      [1,1,0,0,0],
      [1,1,1,1,1],
    ]

So we have a map like this

    integer 0 represents walls

    integer 1 represents valid cells

    cell (0,0) is the starting point (it is the top left corner)

    the bottom right cell is the destination (so this is what we are looking for)

So the solution should be something like this (S represents the states in the solution set):

    [
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,-,-,-,-],
      [S,S,S,S,S],
    ]

Good luck!


"""

from BreadthFirstSearch_solution import maze_bfs # Importamos la función bfs de la clase MazeBFS

def solve_maze(maze): # Definimos la función solve_maze que recibe como parámetro el laberinto
    if not maze or not maze[0]:# Si el laberinto está vacío, devolvemos None
        return []
    
    rows = len(maze) # Obtenemos el número de filas del laberinto
    cols = len(maze[0]) # Obtenemos el número de columnas del laberinto
    start = (0, 0) # Definimos la posición inicial como (0,0)
    end = (rows - 1, cols - 1) # Definimos la posición final como la última fila y columna del laberinto
    
    path = maze_bfs(maze, start, end) # Llamamos a la función bfs de la clase MazeBFS con el laberinto,
    
    if not path: # Si la función bfs devuelve una lista vacía, significa que no hay solución
        return []
    
    solution = [] # Creamos una lista vacía para almacenar la solución
    for r in range(rows): # Recorremos cada fila del laberinto
        solution_row = []
        for c in range(cols): # Recorremos cada columna de la fila
            if (r, c) in path: 
                solution_row.append('S') # Si la posición está en el camino, la marcamos con 'S'
            elif maze[r][c] == 1:
                solution_row.append(1) 
            else:
                solution_row.append(0) 
        solution.append(solution_row)
    
    return solution

if __name__ == '__main__':
    ### Your code must succesfully solve the following mazes:
    
    m = [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]
         ]

    easy_maze = [
        [1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 1]
    ]

    medium_maze = [
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 1]
    ]   
    hard_maze = [
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    print("Solution for maze 'm':") # Imprime la solución para el laberinto 'm'
    solution = solve_maze(m)
    for row in solution:
        print(row)

    print("Solution for maze 'easy_maze':") # Imprime la solución para el laberinto 'easy_maze'
    solution = solve_maze(easy_maze)
    for row in solution:
        print(row)
    
    print("Solution for maze 'medium maze':") # Imprime la solución para el laberinto 'medium_maze' 
    solution = solve_maze(medium_maze)
    for row in solution:
        print(row)

    print("Solution for maze 'hard_maze':") # Imprime la solución para el laberinto 'hard_maze'
    solution = solve_maze(hard_maze)
    for row in solution:
        print(row)