# Distance between two nodes: the length of the shortest path between them

nx.shortest_path(G, 'A','H') # the distance path between node A and # HACK: 
#Output: ['A','B','C','E','H']

nx.shortest_path_length(G, 'A','H') # the distance length
#Output: 4

# Breadth-First Search
T = nx.bfs_tree(G,'A')
T.edges() # Get all edges in the tree 
nx.shortest_path_length(G,'A') 

"""How to characterize the distance between all pairs of nodes in a graph?"""
# Average distance
nx.average_shortest_path_length(G)

# Diameter: maximum distance between any pair of nodes
nx.diameter(G)

# Eccentricity: the eccentricity of a node n is the largest distance between n and all other nodes
nx.eccentricity(G)

# Radius: the minimum eccentricity
nx.radius(G)

"""How to summarize the distances between all pairs of nodes in a graph?"""
# Periphery: the set of nodes that have eccentricity equal to the diameter (maximum eccentricity)
nx.periphery(G)

# Center: the set of nodes that have eccentricity equal to the radius (minimum eccentricity)
nx.center(G)

