# Bipartite Graph: 
# A grahph whose nodes can be split into two sets L and R and every edge connects
# an node in L with a node in R. 

from networkx.algorithms import bipartite
B = nx.Graph() # No separate class for bipartite graphs
B.add_nodes_from(['A','B','C','D','E'], bipartite=0) # label one set of nodes 0
B.add_nodes_from([1,2,3,4], bipartite = 1) # label other set of nodes 1
B.add_edges_from([('A',1),('B',1),('C',1),('C',3),('D',2),('E',3),('F',4)])

# Checking if a graph is bipartite
bipartite.is_bipartite(B)

B.add_edge('A','B')
bipartite.is_bipartite(B)

B.remove_edge('A','B')

# Checking if a set of nodes is a bipartition of a graph
X = set([1,2,3,4])
bipartite.is_bipartite_node_set(B,X)

# L-Bipartite graph projection:
# Network of nodes in group L, where a pair of nodes is connected if they have a
# common neighbor in R in the bipartite graph
B = nx.Graph()
B.add_edges_from([('A',1),('B',1),('C',1),('C',2),('D',2),('E',2),('G',2),
                 ('E',3),('F',3),('H',3),('J',3),('E',4),('I',4),('J',4))]
X = set(['A','B','C','D','E','F','G','H','I','J'])
P = bipartite.projected_graph(B,X)

# L-Bipartite weighted graph projection:
# An L-Bipartite graph projection with weights on the edges that are proportional
# to the number of common neighboers between the add_nodes_from
X = set([1,2,3,4])
P = bipartite.weighted_projected_graph(B,X)



