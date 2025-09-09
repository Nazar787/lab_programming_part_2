import csv
import heapq

def read_adjacency_matrix(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        matrix = [list(map(float, row)) for row in reader]
    return matrix

def prim_mst(matrix):
    N = len(matrix)
    visited = [False] * N
    min_edge = [float('inf')] * N
    min_edge[0] = 0
    heap = [(0, 0)]
    total_length = 0

    while heap:
        weight, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        total_length += weight

        for v in range(N):
            if not visited[v] and 0 < matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]
                heapq.heappush(heap, (matrix[u][v], v))

    return total_length

def main():
    filename = 'islands.csv'
    matrix = read_adjacency_matrix(filename)
    total_length = prim_mst(matrix)
    print(f"Мінімальна довжина кабелю: {total_length:.2f} одиниць")

if __name__ == "__main__":
    main()
