G = nx.Graph()

G.add_edge('A','B', weight=6, relation='family')
G.add_edge('B','C', weight=13, relation='friend')

G.edges() # list of all edges
#Output: [('A','B'), ('C','B')]

G.edges(data=True) # list of all edges with attributes
#Output: [('A','B', {'relation':'family','weight':6})]

G.edges(data='relation') # list of all edges with attribute 'relation'

G.edge['A']['B'] # dictionary of attributes of edge (A,B)
#Output: {'relation':'family','weight':6}

G.edge['B']['C']['weight'] = G.edge['C']['B']['weight'] # undirected graph, order doesn't matter

# Directed, weighted network
G = nx.DiGraph()
G.add_edge('A', 'B', weight=6, relation='family')
G.add_edge('C','B', weight=13, relation='friend')

G.edge['C']['B']['weight'] != G.edge['B']['C']['weight'] # directed graph, order matters

# MultiGraph - undirected graph
G=nx.MultiGraph()
G.add_edge('A','B', weight=6, relation='family')
G.add_edge('A','B', weight = 18, relation = 'friend')
G.add_edge('C','B', weight=13, relation='friend')

# Access the first edge's attribute
G.edge['A']['B']['0']['weight'] # undirected graph, order doesn't matter

# MultiGraph - directed graph: order matters
G=nx.MultiDiGraph()

# Node attributes
G.nodes() # list of all nodes
#Output: ['A','C','B']

G.nodes(data=True) # list of all nodes with attributes
G.node['A']['role']

