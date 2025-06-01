from nodegraph import *

def dsg(P):
    R = graph()
    for i, p in enumerate(P):
        R.add_node(p)
        for j, q in enumerate(P):
            if i==j:
                continue
            if p.dominates(q):
                R.add_edge(p,q)
    return R