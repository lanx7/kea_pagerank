# Test Class Version of PageRank
# -*- coding: utf-8 -*-
import pagerank


nodes = ['A','B','C']
#edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0)]
edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0), ('C','B',1.0)]
#edges = [('A','B', 1.0), ('B','C',1.0), ('C','B',1.0), ('B','A',1.0)]

p = pagerank.PageRank(nodes, edges)
p.print_graph()
print p.get_transition_table()
print p.calc_rank()
