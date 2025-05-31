from mdg import *
from nodegraph import *
from search import *
from visual import *

if __name__ == "__main__":
    # Example usage
    # 12 points in 2D space
    P = [node([1, 9], 1), node([2, 8], 2), node([3, 11], 3),
         node([4, 5], 4), node([5, 12], 5), node([6, 7], 6),
         node([7, 4], 7), node([8, 10], 8), node([9, 1], 9),
         node([10, 6], 10), node([11, 2], 11), node([12, 3], 12)]
    l = 3

    MDG, B = mdg(P, l)
    print("MDG Nodes:")
    for n in MDG.nodes:
        print(n)
    print("\nMDG Edges:")
    for from_node, to_nodes in MDG.edges.items():
        print(f"{from_node} -> {', '.join(map(str, to_nodes))}")
    print("\nParents in MDG:")
    for node, parents in MDG.other.items():
        print(f"{node}: {[str(parent) for parent in parents]}")

    R = p_mds(P, l, MDG, B)
    print("\nPareto Optimal Sets:")
    for r in R:
        print([str(node) for node in r])
    print("\nB Sets:")
    for i, b in enumerate(B):
        print(f"B[{i}]: {[str(node) for node in b]}")

    visualize_graph(MDG)