# Triadic closure: The tendency for people who share connections in a social network to become connected.
# Clustering coef: measures the degree to which in a network tend to 'cluster' or form triangles
G = nx.Graph()
G.add_edges_from([('A','K),('A','B'),('A','C'),('B','C'),('B','K'),
                  ('C','E'),('C','F'),('D','E'),('E','F'),('E','H'),
                  ('F','G'),('I','J')])
# Local clusterig coefficient for node F
nx.clustering(G, 'F')
                  
# Global Clustering Coefficient
""" Measuring clustering on the whole network
Approach 1: Average local clustering coefficient over all nodes in the Graph"""
nx.average_clustering(G)

"""Approcah2: percentaege of open triads that are triangles in a network"""
# Transitivity: ratio of number of triangles and number of open triads in a network
nx.transitivity(G)

                  
