from nodegraph import *

def mdg(P, l):
    G = graph()
    B = []
    parents = {}
    sorted_P = sorted(P, key=lambda x: x.value_sum())
    for i in range(l):
        B.append([])
    for p in sorted_P:
        flag = True
        parents[p] = []
        for i in reversed(range(l)):
            if flag == False:
                break
            for p_ in B[i]:
                if p_.dominates(p):
                    if p_ not in parents[p]:
                        parents[p].append(p_)
                    for parent in parents[p_]:
                        if parent not in parents[p]:
                            parents[p].append(parent)
                    if len(parents[p]) >= l:
                        flag = False
                        break
        if flag:
            G.add_node(p)
            for parent in parents[p]:
                G.add_edge(parent, p)
            if p not in B[len(parents[p])]:
                B[len(parents[p])].append(p)
    G.other = parents
    return G, B