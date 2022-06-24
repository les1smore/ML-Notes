# The degree of a node in an undirected graph is the number of neighbors it has.
# The degree distribution of a graph is the probability of the degrees over the entire network

# Plot of the degree distribution of this network
degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = [list(degree_values().count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

import matplotlib.pyplot
plt.bar(degree_values, histogram)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()

# The in-degree of a node in a directed graph is the number of in-links it has. (node points to it)
in_degrees = G.in_degree()
in_degree_values = sorted(set(in_degrees.values()))
histogram = [list(in_degree_values().count(i)/float(nx.number_of_nodes(G)) for i in in_degree_values]

import matplotlib.pyplot
plt.bar(in_degree_values, histogram)
plt.xlabel('In Degree')
plt.ylabel('Fraction of Nodes')
plt.show()

