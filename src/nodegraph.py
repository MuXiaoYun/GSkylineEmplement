class node:
    def __init__(self, value, nodeid=-1):
        self.value = value
        self.nodeid = nodeid  

    def __repr__(self):
        return f"Node({self.value}, id={self.nodeid})"
    
    def value_sum(self):
        return sum(a for a in self.value)
    
    def dominates(self, other):
        return all(a <= b for a, b in zip(self.value, other.value)) and any(a < b for a, b in zip(self.value, other.value))
    
    def equals(self, other):
        return all(a == b for a, b in zip(self.value, other.value)) and len(self.value) == len(other.value)
    
class graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.other = None  # Placeholder for any additional attributes

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, from_node, to_node):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges[from_node]:
            self.edges[from_node].append(to_node)
        if to_node not in self.nodes:
            self.nodes.append(to_node)
        if from_node not in self.nodes:
            self.nodes.append(from_node)

    