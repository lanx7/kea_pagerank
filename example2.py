# Test Matrix Version of PageRank

# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

def get_inlink(node):
    global G
    edges = G.in_edges(node)
    result = []
    for e in edges:
        result.append(e[0])
    print "Inlink of %s" % node,result
    return result

def get_outlink(node):
    global G
    edges = G.out_edges(node)
    result = []
    for e in edges:
        result.append(e[1])
    print "Outlink of %s" % node, result
    return result

def idx(node):
    global nodes
    return sorted(nodes).index(node)

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

# Initializing Array
nodes = G.nodes()
N = len(nodes)
P = np.zeros((N,N))
r = np.zeros(N)
d = 0.7
rs = np.zeros(N)

for n in nodes:
    out_nodes = get_outlink(n)
    print n, out_nodes
    weight_sum = sum(list(map(lambda x : G.edge[n][x]['weight'], out_nodes)))
    print "WS", weight_sum
    for o in out_nodes:
        P[idx(n),idx(o)] = G.edge[n][o]['weight']/weight_sum # Weight Graph Version
        #print n, o, G.edge[n][o]['weight'], weight_sum
        #P[idx(n),idx(o)] = 1.0/len(out_nodes) # No Weight Version (Weight == 1.0)

    r[idx(n)] = G.node[n]['PR']
    rs[idx(n)] = 1.0/N

print P
print r

for i in xrange(10):
    r_old = r.copy()

    r = d*np.dot(P.T,r)+(1-d)*rs # Page Rank Core Algorithm

    print r
    if np.array_equal(r_old,r) == True:
        print 'Final Result at %d' % i, r
        break
