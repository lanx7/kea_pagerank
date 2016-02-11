# Test Class Version of PageRank
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np
import pagerank

# Constructing Graph
G = nx.DiGraph()

nodes = ['A','B','C']
#edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0)]
edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0), ('C','B',1.0)]
#edges = [('A','B', 1.0), ('B','C',1.0), ('C','B',1.0), ('B','A',1.0)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
G.node['A']['PR'] = 0.33
G.node['B']['PR'] = 0.33
G.node['C']['PR'] = 0.33

print(G.nodes(data=True))
print(G.edges(data=True))

pr = pagerank.PageRank(G)
print pr.get_transition_table()
print pr.get_restart()
print pr.get_rank()
print pr.calc_rank()
print pr.get_rank()