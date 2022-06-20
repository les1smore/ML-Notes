# Network robustness
"""The ability of a network to maintain its general structural properties when it faces failures or attacks

Type of attacks: removal of nodes or edges

Structural properties: connectivity

Examples: airport closures, internet router failures, power line failures

"""

# Disconnecting a Graph
"""What is the smallest number of nodes that can be removed from this graph in order to disconnect it?"""
nx.node_connectivity(G_un) # the number of nodes to remove
nx.minimum_node_cut(G_un) # which node? 

"""What is the smallest number of edges that can be removed from this graph in order to disconnect it?"""
nx.edge_connectivity(G_un) # the number of edges to remove
nx.minimum_edge_cut(G_un) # which edge? 

"""Imagine node G wants to send a message to node L by passing it along to other nodes in this network,
    What options does G have to deliver the message?"""
sorted(nx.all_simple_paths(G, 'G','L'))

"""If we wanted to block the message from G to L by removing nodes from the network, how many nodes would we need to remove?"""
nx.node_connectivity(G, 'G','L') # the number of nodes to remove
nx.minumum_node_cut(G, 'G','L') # which node?

"""If we wanted to block the message from G to L by removing edges from the network, how many edges would we need to remove?"""
nx.edge_connectivity(G, 'G','L') # the number of edges to remove
nx.minumum_edge_cut(G, 'G','L') # which edge?  


