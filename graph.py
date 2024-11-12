def is_safe(graph, vertex, colors, color):
    # Check if any adjacent vertex has the same color
    for neighbor in graph[vertex]:
        if colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, m, colors, vertex):
    # If all vertices are assigned a color, print the solution
    if vertex == len(graph):
        print("Solution:", colors)
        return True

    found_solution = False
    # Try all colors for the current vertex
    for color in range(1, m + 1):
        if is_safe(graph, vertex, colors, color):
            colors[vertex] = color  # Assign color to the vertex
            # Recursively color the next vertex
            if graph_coloring(graph, m, colors, vertex + 1):
                found_solution = True
            colors[vertex] = 0  # Backtrack

    return found_solution


def solve(graph, m):
    colors = [0] * len(graph)  # Initialize colors of all vertices to 0
    if not graph_coloring(graph, m, colors, 0):
        print("No solution exists")

# Example graph: adjacency list representation
graph = [[1, 2], [0, 2], [0, 1]]
m = 3  # Number of colors
solve(graph, m)
