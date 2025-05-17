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

def maze_bfs(maze, start, end):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    
    if maze[start[0]][start[1]] != 1 or maze[end[0]][end[1]] != 1:
        return None
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    start_node = MazeNode(start)
    queue.append(start_node)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    while queue:
        current_node = queue.popleft()
        row, col = current_node.position
        
        if (row, col) == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                maze[new_row][new_col] == 1 and not visited[new_row][new_col]):
                visited[new_row][new_col] = True
                new_node = MazeNode((new_row, new_col), current_node)
                queue.append(new_node)
    
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