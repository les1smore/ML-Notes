# Triadic closure: The tendency for people who share connections in a social network to become connected.

G = nx.Graph()
G.add_edges_from([('A','K),('A','B'),('A','C'),('B','C'),('B','K'),
                  ('C','E'),('C','F'),('D','E'),('E','F'),('E','H'),
                  ('F','G'),('I','J')])
# Local clusterig coefficient for node F
nx.clustering(G, 'F')
                  
# Global Clustering Coefficient
                  
