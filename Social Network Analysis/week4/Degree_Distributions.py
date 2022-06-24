degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = [list(degree_values().count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

import matplotlib.pyplot
