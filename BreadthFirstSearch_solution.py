from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False

def breadth_first_search(start_node):
    queue = [start_node]
    while queue:
        actual_node = queue.pop(0)
        actual_node.visited = True
        print(actual_node.name)
        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)


class MazeNode:
    def __init__(self, position, parent=None):
        self.position = position  # (row, col)
        self.parent = parent
        self.visited = False

def maze_bfs(maze, start, end): # Es la funcion que se encarga de encontrar el camino más corto en el laberinto
    rows = len(maze) # Obtenemos el número de filas del laberinto
    cols = len(maze[0]) if rows > 0 else 0 # Obtenemos el número de columnas del laberinto
    
    if maze[start[0]][start[1]] != 1 or maze[end[0]][end[1]] != 1:
        return None # Si la posición de inicio o fin no es un 1, no hay camino
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Arriba, abajo, izquierda, derecha
    queue = deque() # Creamos una cola para BFS
    start_node = MazeNode(start) # Creamos un nodo para la posición de inicio
    queue.append(start_node) # Agregamos el nodo a la cola
    visited = [[False for _ in range(cols)] for _ in range(rows)] # Creamos una matriz para marcar las posiciones visitadas
    visited[start[0]][start[1]] = True # Marcamos la posición de inicio como visitada
    
    while queue: 
        current_node = queue.popleft() # Sacamos el primer nodo de la cola
        row, col = current_node.position  # Obtenemos la posición del nodo actual
        
        if (row, col) == end: 
            path = [] # Creamos una lista para almacenar el camino
            while current_node: 
                path.append(current_node.position) # Agregamos la posición del nodo actual al camino
                current_node = current_node.parent # Movemos la posición del nodo actual a su padre
            return path[::-1]  # Retornamos el camino inverso
        
        for dr, dc in directions: # Recorremos las posiciones adyacentes
            new_row, new_col = row + dr, col + dc # Calculamos la posición nueva
            if (0 <= new_row < rows and 0 <= new_col < cols and  
                maze[new_row][new_col] == 1 and not visited[new_row][new_col]): # Verificamos si la posición nueva es válida
                visited[new_row][new_col] = True # Marcamos la posición nueva como visitada
                new_node = MazeNode((new_row, new_col), current_node) # Creamos un nuevo nodo para la posición nueva
                queue.append(new_node) # Agregamos el nodo a la cola
    
    return None

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    print("BFS example:")
    breadth_first_search(node2)