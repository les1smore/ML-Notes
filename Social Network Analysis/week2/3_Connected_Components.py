# Connectivity in Undirected Graphs
"""Connected Component: 
1. Every node in the subset has a paht to every other node
2. No other node has a path to any node in the subset"""
nx.number_connected_components(G)

sorted(nx.number_connected_components(G)) # Get the see the edges inside the subsets

nx.node_connected_component(G, 'M') # which connected component the edge 'M' belongs to 

 
# Connectivity in Directed Graphs
"""A directed graph is strongly connected if, for every pair nodes u and v, there is a directed path from u to v
   and a directed path from v to u."""
nx.is_strongly_connected(G)

"""A directed graph is weakly connected if replacing all directed edges with undirected edges produces a connected undirected graph"""
nx.is_weakly_connected(G)


# Strongly connected component:
""" 1. Every node in the subset has a directed path to every other nodes
    2. No other node has a directed path to and from every node in the subset"""
sorted(nx.strongly_connected_components(G))

# Weakly connected component:
"""The connected components of the graph after replacing all directed edges with undirected edges."""
sorted(nx.weakly_connected_components(G)) # Since the graph is weakly connected it only has one weakly connected component (the whole network itself)


