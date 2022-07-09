"""
Breadth First Search
    - Starts at any node and explores ALL neighbours first, before moving to the next level of neighbours.

Application of BFS Algorithm
    - The Shortest path on unweighted graph

Time complexity: O(V+E), number vertices and edges
Space complexity: O(V)

https://www.youtube.com/watch?v=oDqjPvD54Ss
https://www.programiz.com/dsa/graph-bfs
"""


def bfs(visited, graph, node):
    visited = [node]  # List for visited nodes
    queue = []

    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }

    bfs(graph, '5')
