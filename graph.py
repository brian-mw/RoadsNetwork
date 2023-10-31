class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, value):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = value
    
    def get_nodes(self):
        return list(self.graph.keys())