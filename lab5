from collections import deque

def parse_input(data):
    lines = data.strip().split('\n')
    start = tuple(map(int, lines[0].split(',')))
    end = tuple(map(int, lines[1].split(',')))
    rows, cols = map(int, lines[2].split(','))
    matrix = [list(map(int, line.split())) for line in lines[3:]]
    return start, end, rows, cols, matrix

def is_valid(x, y, rows, cols, matrix, visited):
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and not visited[x][y]

def bfs_shortest_path(start, end, rows, cols, matrix):
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, rows, cols, matrix, visited):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    return -1
