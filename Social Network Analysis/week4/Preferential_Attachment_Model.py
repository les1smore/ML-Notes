# barabasi_albert_graph(n,m) to construct a n-node preferential attachment network, where each new node attaches to m existing nodes.
G = nx.barabasi_albert_graph(1000000,1) # one network with 1000000 nodes
degrees = G.degree()
degree_values = sorted(set(degrees.values()))
histogram = [list(degrees.values().count(i)/float(nx.number_of_nodes(G)) for i in degree_values]

plt.plot(degree_values,histogram,'o')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()
