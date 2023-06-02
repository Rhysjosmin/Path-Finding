import sys

def dijkstra(graph, start):
    # Initialize distances and visited array
    distances = [sys.maxsize] * len(graph)
    distances[start] = 0
    visited = [False] * len(graph)

    # Dijkstra's Algorithm
    for _ in range(len(graph)):
        # Find the vertex with the minimum distance
        min_distance = sys.maxsize
        min_index = -1
        for v in range(len(graph)):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        # Mark the vertex as visited
        visited[min_index] = True

        # Update the distances of adjacent vertices
        for v in range(len(graph)):
            if (not visited[v]) and (graph[min_index][v] != 0) and (distances[min_index] + graph[min_index][v] < distances[v]):
                distances[v] = distances[min_index] + graph[min_index][v]

    return distances

# Example usage
graph = [
    [0, 4, 2, 0, 0, 0],
    [4, 0, 1, 5, 0, 0],
    [2, 1, 0, 8, 10, 0],
    [0, 5, 8, 0, 2, 6],
    [0, 0, 10, 2, 0, 3],
    [0, 0, 0, 6, 3, 0]
]

start_vertex = 0

distances = dijkstra(graph, start_vertex)

# Display the shortest path distances
print("Shortest path distances from vertex", start_vertex, "to all other vertices:")
for i, distance in enumerate(distances):
    print("Vertex", i, ":", distance)

