from nodegraph import *

def is_skyline(P, node):
    for other in P:
        if other != node and other.dominates(node):
            return False
    return True

def get_parent_number(B, p):
    for i in range(len(B)):
        if p in B[i]:
            return i
    assert False, "Parent not found in B"

def p_mds(P, l, MDG: graph, B):
    R = []
    gr = []
    MDG.nodes.sort(key=lambda x: get_parent_number(B, x))
    for p in MDG.nodes:
        if is_skyline(P, p):
            gr = [p]
            search_single(gr, p, R, l, MDG)
    return R

def search_single(gr:list, plast, R, l, MDG):
    if len(gr) == l:
        R.append(gr.copy())
        return
    index_plast = -1
    for i in range(len(MDG.nodes)):
        if MDG.nodes[i] == plast:
            index_plast = i
            break
    for i in range(index_plast + 1, len(MDG.nodes)):
        flag = True
        for en in MDG.other[MDG.nodes[i]]:
            if en not in gr:
                flag = False
                break
        if flag:
            gr.append(MDG.nodes[i])
            search_single(gr, MDG.nodes[i], R, l, MDG)
            gr.pop()