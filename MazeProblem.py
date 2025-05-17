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

from BreadthFirstSearch_solution import maze_bfs

def solve_maze(maze):
    if not maze or not maze[0]:
        return []
    
    rows = len(maze)
    cols = len(maze[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    
    path = maze_bfs(maze, start, end)
    
    if not path:
        return []
    
    solution = []
    for r in range(rows):
        solution_row = []
        for c in range(cols):
            if (r, c) in path:
                solution_row.append('S')
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

    print("Solution for maze 'm':")
    solution = solve_maze(m)
    for row in solution:
        print(row)

    print("Solution for maze 'easy_maze':")
    solution = solve_maze(easy_maze)
    for row in solution:
        print(row)
    
    print("Solution for maze 'medium maze':")
    solution = solve_maze(medium_maze)
    for row in solution:
        print(row)

    print("Solution for maze 'hard_maze':")
    solution = solve_maze(hard_maze)
    for row in solution:
        print(row)