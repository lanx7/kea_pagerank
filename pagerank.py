# PR(A) = (1-d)/N + d(PR(T1)/C(T1)+...+ PR(Tn)/C(tn))
# r(t+1) = (d)*P*r(t) + (1-d)rs
# P (Transition Matrix), rs(restart vector)
import networkx as nx
import numpy as np
from utils import *

class PageRank():
    d = 0.7             # Dampling Factor
    def __init__(self, graph):
        G = self.graph = graph
        nodes = self.graph.nodes()
        N = len(nodes)
        self.P = np.zeros((N,N))
        self.r = np.zeros(N)
        self.rs = np.zeros(N)

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
            self.rs[idx(G,n)] = 1.0/N

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
        return self.r

    def get_restart(self):
        return self.rs