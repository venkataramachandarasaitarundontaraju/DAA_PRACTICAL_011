from typing import List, Optional, Tuple

def floyd_warshall(
    vertices_count: int, 
    graph_matrix: List[List[float]]
) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
    dist: List[List[float]] = [list(row) for row in graph_matrix]
    
    next_node: List[List[Optional[int]]] = [
        [None for _ in range(vertices_count)] for _ in range(vertices_count)
    ]
    
    for i in range(vertices_count):
        for j in range(vertices_count):
            if graph_matrix[i][j] != float('inf') and i != j:
                next_node[i][j] = j

    for k in range(vertices_count):
        for i in range(vertices_count):
            for j in range(vertices_count):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def construct_path(u: int, v: int, next_node: List[List[Optional[int]]]) -> List[int]:
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]  # type: ignore
        if u is None:
            return []
        path.append(u)
    return path

if __name__ == "__main__":
    INF = float('inf')
    V = 4

    input_graph: List[List[float]] = [
        [0.0, 3.0, INF, 7.0],
        [8.0, 0.0, 2.0, INF],
        [5.0, INF, 0.0, 1.0],
        [2.0, INF, INF, 0.0]
    ]

    distance_matrix, route_matrix = floyd_warshall(V, input_graph)

    print("--- Shortest Distance Matrix ---")
    for row in distance_matrix:
        print(" ".join(f"{val:5.1f}" if val != INF else "  INF" for val in row))

    print("\n--- Exact Node Paths ---")
    start_node = 0
    end_node = 2
    shortest_path = construct_path(start_node, end_node, route_matrix)
    
    if shortest_path:
        path_str = " -> ".join(map(str, shortest_path))
        print(f"Path from Node {start_node} to Node {end_node}: {path_str}")
        print(f"Total Distance: {distance_matrix[start_node][end_node]}")
    else:
        print(f"No path exists between Node {start_node} and Node {end_node}")
