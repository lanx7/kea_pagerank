import networkx as nx
from utils import *
G = nx.DiGraph()

#G = nx.Graph()

nodes = ["A","B","C"]
edges = [('A','B',1.0), ('B','C',1.0)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
G.add_edge('B','C')
G.add_edge('C','A')
G.add_edge('A','C')
for (u,v,d) in G.edges(data='weight'):
    print u,v,d
print(G.nodes())
print(G.edges())
print(G.out_edges('A'))
print(G.in_edges('A'))

"""
K = nx.Graph()
H = nx.path_graph(10)
K.add_nodes_from(H)
print(K.nodes())
print(K.edges())
"""
print idx(G, 'A')