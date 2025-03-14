import random

def generate_random_tree(n):
    if n <= 1:
        return []
    
    edges = []  # Stores the tree edges
    nodes = {0}  # Start with the first node
    available = list(range(1, n))  # Remaining nodes to connect
    
    while available:
        new_node = random.choice(available)  # Pick a random node
        existing_node = random.choice(list(nodes))  # Connect to an existing node
        edges.append((existing_node, new_node))  # Add edge
        nodes.add(new_node)  # Add to connected nodes
        available.remove(new_node)  # Remove from available
    
    return edges

# Example usage:
n = 10  # Number of nodes
tree_edges = generate_random_tree(n)
print("Random Tree Edges:", tree_edges)
