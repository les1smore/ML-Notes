# Degree Centrality
"""Assumption: important nodes have many connections - number of neighbors"""
# Degree Centrality - Undirected Networks
"""C(v) = dv/|N|-1, where N is the set of nodes in the network and dv is the degree of node v"""
G = nx.karate_club_graph()
G = nx.convert_node_labels_to_integers(G, first_label=1)
degCent = nx.degree_centrality(G)
degCent[34]

# Degree Centrality - Directed Networks
"""C(v) = dv(in) / |N|-1, where N = set of nodes in the network, dv(in) = in-degree of node v"""
indegCent = nx.in_degree_centrality(G)
indegCent['A']
"""C(v) = dv(out) / |N|-1, where N = set of nodes in the network, dv(out)= the out-degree of node v"""
outdegCent = nx.out_degree_centrality(G)
outdegCent['A']

# Closeness Centrality
# The closeness centrality of nodes that cannot reach any other nodes is always 0.
# The highest closeness centrality occurs when the node can only reach one node and it reachs in one step.
"""Assumption: important nodes are close to other nodes"""
closeCent = nx.closeness_centrality(G)
closeCent[32]

sum(nx.shortest_path_length(G,32).values()) # Output is 61
(len(G.nodes()-1)/61) # Output = closeCent[32]

"""Measure the closeness centrality of a node when it cannot reach all other nodes"""
closeCent = nx.closeness_centrality(G, normalized=False)
closeCent['L']
#Output:1

closeCent = nx.closeness_centrality(G, normalized=True) # normalized example
closeCent['L']
#Output:0.071

# Betweenness centrality
btwnCent = nx.betweenness_centrality(G, normalized=True, endpoints=False)

import operator
sorted(btwnCent.items(), key = operator.itemgetter(1), reverse=True)[0:5] # top 5 nodes with largest betweenness Centrality

btwnCent = nx.betweenness_centrality(G, normalized=True, endpoints=False, k = 10) # approximation 10 sample nodes
btwnCent_subset = nx.betweenness_centrality(G, [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                            [1, 4, 13, 11, 6, 12, 17, 7], normalized = True) # subset nodes

btwnCent_edge = nx.edge_betweenness_centrality(G, normalized = True) # BC of edges
btwnCent_edge_subset = nx.edge_betweenness_centrality(G, [34, 33, 21, 30, 16, 27, 15, 23, 10],
                                            [1, 4, 13, 11, 6, 12, 17, 7], normalized = True) # subset edges
