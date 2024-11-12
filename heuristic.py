# First, we define our graph structure
# This is a dictionary where:
# - Keys are nodes (A, B, C, etc.)
# - Values are lists of tuples (neighbor, distance)
Graph_nodes = {
    'A': [('B', 6), ('C', 3)],     # Node A connects to B(distance 6) and C(distance 3)
    'B': [('D', 4), ('E', 5)],     # Node B connects to D(distance 4) and E(distance 5)
    'C': [('F', 7), ('E', 2)],     # Node C connects to F(distance 7) and E(distance 2)
    'E': [('F', 8), ('D', 6)],     # Node E connects to F(distance 8) and D(distance 6)
}

# 1. First function: get_neigh (Get Neighbors)
# This function returns all neighbors of a given node
def get_neigh(v):
    if v in Graph_nodes:
        return Graph_nodes[v]  # Returns list of neighbors and their distances
    else:
        return []             # Returns empty list if node not found

# 2. Second function: h (Heuristic)
# This estimates the cost from any node to the goal
def h(n):
    H_dist = {
        'A': 10,
        'B': 15,
        'C': 19,
        'D': 9,
        'E': 12,
        'F': 11,
    }
    return H_dist.get(n, float('inf'))  # Returns infinity if node not found

# 3. Main A* algorithm function
def a_star(start, stop):
    # Initialize sets and dictionaries
    open_set = set([start])      # Nodes to be evaluated
    closed_set = set()           # Nodes already evaluated
    g = {start: 0}              # Cost from start to node
    parents = {start: start}     # Keep track of path
    
    while open_set:  # While there are nodes to evaluate
        n = None
        # Find node with lowest f(n) = g(n) + h(n)
        for v in open_set:
            if n is None or g[v] + h(v) < g[n] + h(n):
                n = v
                
        # If no path exists
        if n is None:
            print("Path does not exist!")
            return None
            
        # If we reached the goal
        if n == stop:
            path = []
            # Reconstruct path
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("Path found:", path)
            return path
            
        # Explore neighbors
        for (m, weight) in get_neigh(n):
            # If neighbor not evaluated yet
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                # If we found a better path
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)
                        
        # Move current node to closed set
        open_set.remove(n)
        closed_set.add(n)
    
    print("Path not found!")
    return None

# Test the algorithm
print("Finding path from A to F:")
a_star('A', 'F')