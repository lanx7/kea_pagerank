# -*- coding: utf-8 -*-
import networkx as nx

def page_rank_value(node):
    global G
    return G.node[node]['PR']

def get_inlink(node):
    global G
    edges = G.edges()
    result = []
    for e in edges:
        #print e, e[1]
        if node == e[1]:
            #print 'got it'
            result.append(e[0])
    #print "Inlink of %s" % node,result
    return result

def get_outlink(node):
    global G
    edges = G.edges()
    result = []
    for e in edges:
        #print e, e[1]
        if node == e[0]:
            #print 'got it'
            result.append(e[1])
    #print "Outlink of %s" % node, result
    return result


def page_rank_simple(node, path):
    global G
    d = 0.7
    N = len(G.nodes())
    #if node in path:
    #    return initial_pr(node)
    node_adjs = get_inlink(node)
    my_pr = 0.0

    for adj in node_adjs: # for node로 들어오는 모든 link에 대해
        n_link = len(get_outlink(adj))
        try:
            my_pr += page_rank_value(adj) / n_link
            print "My_PR: %f, PR_ADJ: %f, n: %d" % (my_pr, page_rank_value(adj), n_link)
        except ZeroDivisionError:
            print "Error: Outlink of %s is Zero" % n_link
    # link 출발점 노드의 Pare_rank계산z
    my_pr = (1-d)/N + d * my_pr
    print "PageRank: %f" % my_pr
    #G.node[node]['PR'] = my_pr
    return my_pr

def page_rank_matrix(node, path):
    global G
    return

def update(r):
    global G
    for v in r:
        G.node[v[0]]['PR'] = v[1]

G = nx.DiGraph()

nodes = ['A','B','C']
#edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0)]
edges = [('A','B', 1.0), ('B','C',1.0), ('C','A',1.0), ('C','B',1.0)]


G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)
G.node['A']['PR'] = 0.33
G.node['B']['PR'] = 0.33
G.node['C']['PR'] = 0.33

print(G.nodes(data=True))
print(G.edges(data=True))

nodes = G.nodes()

for i in xrange(10):
    r = []
    for n in nodes:
        print "Node:", n
        print "Initial_Value", page_rank_value(n)
        #get_inlink(n)
        #get_outlink(n)
        result = page_rank_simple(n,[])
        r.append((n,result))
    update(r)

print G.nodes(data=True)