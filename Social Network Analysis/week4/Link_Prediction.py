# Measure 1: Common Neighbors
common_neigh = [(e[0], e[1], len(list(nx.common_neighbors(G, e[0], e[1])))) for e in nx.non_edges(G)]
sorted(common_neigh, key=operator.itemgetter(2), reverse=True)
print(common_neigh)

# Measure 2: Jaccard Coefficient
# Number of common neighbors normalized by the total number of neighbors
L = list(nx.jaccard_coefficient(G))
L.sort(key=operator.itemgetter(2), reverse=True)
print(L)

# Measure 3: Resource Allocation
# The number of common neighbors / the in-degree depth of each common neighbor node
L = list(nx.resource_allocation_index(G))
L.sort(key=operator.itemgetter(2), reverse=True)
print(L)

# Measure 4: Adamic-Adar
# # The number of common neighbors / log scale the in-degree depth of each common neighbor node

# Measure 5: Pref.Attachment
# In the preferential attachment model, nodes with high degree get more neighbors
# Pref_attach(X,Y) = |N(X)|*|N(Y)|
L = list(nx.preferential_attachment(G))
L.sort(key=operator.itemgetter(2), reverse=True)
print(L)

# Measure 6: Community Structure
# The community structure of the network for link prediction
# Assume the nodes in this network belong to different communities (sets of nodes)
# Pairs of nodes who belong to the same community and have many common neighbors in their community are likely to form an edge.
= # of common neighbors + bonus (1, if the common neighbor is in the same community as X and Y or else 0)
G.node['A']['community'] = 0 # Assign nodes to different communities
G.node['B']['community'] = 0
G.node['C']['community'] = 0
G.node['D']['community'] = 0
G.node['E']['community'] = 1
G.node['F']['community'] = 1
G.node['G']['community'] = 1
G.node['H']['community'] = 1
G.node['I']['community'] = 0

L = list(nx.cn_soundarajan_hopcroft(G))
sort(key=operator.itemgetter(2), reverse=True)
print(L)

# Measure 7: Community Resource Allocation
# Similar to resource allocation index, but only considering nodes in the same community
# If the two nodes are from different communities, the value is 0.
L = list(nx.ra_index_soundarajan_hopcroft(G))
L.sort(key=operator.itemgetter(2), reverse=True)
print(L)

