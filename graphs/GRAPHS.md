# [Graphs](https://github.com/Rustam-Z/data-structures-and-algorithms#graphs)

Need to learn:
- DFS (depth first search), stack
- BFS (breadth first search), queue
- Dijkstra's algorithm
- Prim's algorithm (Minimum spanning tree)
- Kruskal's algorithm
 

Notes:
- Vertices (nodes), edges (lines between vertices)
- A tree is a graph, but not all graphs are trees. Tree is connected graph without cycles.
- A graph is a collection of nodes with edges between some of them.
- Directed (one way street) / undirected graph (two way street)  

DFS:
- DFS is often preferred if we want to visit every node in the graph
- It is a bit simpler
- Will not find shortest path

BFS:
- Shortest path between two nodes
- Example: find a path of friendship between A and B. DFS will do deep. But with BFS, we will stay close to nodes neighbors. We will not go to distant connections until absolutely necessary.

