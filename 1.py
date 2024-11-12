# Modified A* implementation with heuristics
def astar_with_heuristic(graph, start, goal, heuristics):
    """
    A* pathfinding with heuristic values.    
    Args:
        graph: Dictionary of node connections {'A': [('B', 4), ('C', 1)]}
        start: Starting node (e.g., 'A')
        goal: Target node (e.g., 'D')
        heuris
        tics: Dictionary of heuristic values {'A': 5, 'B': 3, ...}
    """
    g_costs = {start: 0}  # Actual cost from start
    
    f_costs = {start: heuristics[start]}  # f_cost = g_cost + h_cost
    came_from = {start: None}
    open_nodes = [start]
    
    print("\nStarting A* Search with Heuristics:")
    
    while open_nodes:
        current = min(open_nodes, key=lambda x: f_costs[x])
        
        print(f"\nCurrent Node: {current}")
        print(f"g_cost (actual cost from start): {g_costs[current]}")
        print(f"h_cost (heuristic to goal): {heuristics[current]}")
        print(f"f_cost (total estimated cost): {f_costs[current]}")
        
        if current == goal:
            path = []
            total_cost = g_costs[current]
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1], total_cost
        
        open_nodes.remove(current)
        
        for neighbor, distance in graph[current]:
            g_cost = g_costs[current] + distance
            
            if neighbor not in g_costs or g_cost < g_costs[neighbor]:
                came_from[neighbor] = current
                g_costs[neighbor] = g_cost
                f_costs[neighbor] = g_cost + heuristics[neighbor]
                
                if neighbor not in open_nodes:
                    open_nodes.append(neighbor)
                print(f"Updated {neighbor}:")
                print(f"  g_cost: {g_cost}")
                print(f"  h_cost: {heuristics[neighbor]}")
                print(f"  f_cost: {f_costs[neighbor]}")
    
    return None, None

# Let's create a simple grid-based example:
#
#   A --- B --- C
#   |     |     |
#   D --- E --- F
#   |     |     |
#   G --- H --- I

def test_astar_with_heuristic():
    # Graph with distances (edge weights)
    graph = {
        'A': [('B', 4), ('D', 3)],
        'B': [('A', 4), ('C', 4), ('E', 3)],
        'C': [('B', 4), ('F', 3)],
        'D': [('A', 3), ('E', 4), ('G', 3)],
        'E': [('B', 3), ('D', 4), ('F', 4), ('H', 3)],
        'F': [('C', 3), ('E', 4), ('I', 3)],
        'G': [('D', 3), ('H', 4)],
        'H': [('G', 4), ('E', 3), ('I', 4)],
        'I': [('F', 3), ('H', 4)]
    }
    
    # Heuristic values (straight-line distance to goal 'I')
    heuristics = {
        'A': 8,  # Furthest from I
        'B': 7,
        'C': 6,
        'D': 6,
        'E': 5,
        'F': 3,
        'G': 4,
        'H': 3,
        'I': 0   # Goal has h=0
    }
    
    # Find path from A to I
    path, cost = astar_with_heuristic(graph, 'A', 'I', heuristics)
    
    if path:
        print(f"\nFound path: {' → '.join(path)}")
        print(f"Total actual cost: {cost}")
    else:
        print("\nNo path found!")

# Run the test
test_astar_with_heuristic()