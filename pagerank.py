# PR(A) = (1-d)/N + d(PR(T1)/C(T1)+...+ PR(Tn)/C(tn))
# r(t+1) = (d)*P*r(t) + (1-d)rs
# P (Transition Matrix), rs(restart vector)
import networkx as nx
import numpy as np
from utils import *

class PageRank():
    d = 0.7             # Dampling Factor
    def __init__(self, nodes, edges):
        self.graph = nx.DiGraph()
        self.V = len(nodes)
        node_names = [n[0] for n in nodes]
        self.graph.add_nodes_from(node_names, PR = 1.0/self.V)
        self.graph.add_weighted_edges_from(edges)

        for n in nodes:
            name = n[0]; weight =n[1]
            self.graph.node[name]['weight'] = weight

        self.P = np.zeros((self.V,self.V))
        self.r = np.zeros(self.V)
        self.rs = np.zeros(self.V)


        self.calc_transition_table()

    def calc_transition_table(self):
        G = self.graph
        nodes = G.nodes()

        for n in nodes:
            out_nodes = get_outlink(G, n)
            #print n, out_nodes
            weight_sum = sum(list(map(lambda x : G.edge[n][x]['weight'], out_nodes)))
            #print "WS", weight_sum
            for o in out_nodes:
                self.P[idx(G,n),idx(G,o)] = G.edge[n][o]['weight']/weight_sum # Weight Graph Version
                #print n, o, G.edge[n][o]['weight'], weight_sum
                #P[idx(n),idx(o)] = 1.0/len(out_nodes) # No Weight Version (Weight == 1.0)

            self.r[idx(G,n)] = G.node[n]['PR']
            #self.rs[idx(G,n)] = 1.0/self.V
            self.rs[idx(G,n)] = G.node[n]['weight']

        sum_rs = sum(self.rs)
        self.rs = self.rs / float(sum_rs) # Vector / Scalar
        #self.rs[:] = [float(n)/sum_rs for n in self.rs]
        #self.rs = map(lambda x: float(x)/sum_rs, self.rs)
        print type(self.rs)
        print 'restart vector', self.rs

    def calc_rank(self):
        for i in xrange(100):
            r_old = self.r.copy()
            self.r = self.d*np.dot(self.P.T, self.r)+(1-self.d)*self.rs # Page Rank Core Algorithm
            if np.array_equal(r_old,self.r) == True:
                print 'Final Result at %d' % i, self.r
                break
        return self.r

    def get_transition_table(self):
        return self.P

    def get_rank(self):
        nodes = sorted(self.graph.nodes())
        return zip(nodes,self.r)

    def get_restart(self):
        return self.rs

    def print_graph(self):
        print(self.graph.nodes(data=True))
        print(self.graph.edges(data=True))

    def set_restart_vector(self, vector):
        self.rs = vector.copy()

"""
    def __init__(self, graph):
        self.V = len(nodes)
        self.P = np.zeros((self.V,self.V))
        self.r = np.zeros(self.V)
        self.rs = np.zeros(self.V)

        for n in nodes:
            out_nodes = get_outlink(G, n)
            #print n, out_nodes
            weight_sum = sum(list(map(lambda x : G.edge[n][x]['weight'], out_nodes)))
            #print "WS", weight_sum
            for o in out_nodes:
                self.P[idx(G,n),idx(G,o)] = G.edge[n][o]['weight']/weight_sum # Weight Graph Version
                #print n, o, G.edge[n][o]['weight'], weight_sum
                #P[idx(n),idx(o)] = 1.0/len(out_nodes) # No Weight Version (Weight == 1.0)

            self.r[idx(G,n)] = G.node[n]['PR']
            self.rs[idx(G,n)] = 1.0/self.V
"""