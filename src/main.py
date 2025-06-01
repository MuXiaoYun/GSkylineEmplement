from mdg import *
from dsg import *
from nodegraph import *
from search import *
from visual import *
from readdata import *

if __name__ == "__main__":
    # Example usage
    # 12 points in 2D space
    P, l = read_data()

    DSG = dsg(P)
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

    visualize_graph(DSG, MDG, R)