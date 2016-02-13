import networkx as nx

def get_inlink(graph, node):
    edges = graph.in_edges(node)
    result = []
    for e in edges:
        result.append(e[0])
    #print "Inlink of %s" % node,result
    return result

def get_outlink(graph, node):
    edges = graph.out_edges(node)
    result = []
    for e in edges:
        result.append(e[1])
    #print "Outlink of %s" % node, result
    return result

def idx(graph, node):
    nodes = graph.nodes()
    return sorted(nodes).index(node)