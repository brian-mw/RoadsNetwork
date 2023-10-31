class RoadNetwork:
    def __init__(self, nodes, graph):
        self.nodes = nodes
        self.graph = graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_links(self, node):
        connections = []
        if node in self.graph:
            connections = list(self.graph[node].keys())
        return connections

    def value(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            return self.graph[node1][node2]
        return float("inf")

    def dijkstra(self, start_node):
        unvisited_nodes = list(self.get_nodes())
        shortest_path = {}
        previous_nodes = {}

        max_value = float("inf")
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[start_node] = 0

        while unvisited_nodes:
            current_node = None
            for node in unvisited_nodes:
                if current_node is None:
                    current_node = node
                elif shortest_path[node] < shortest_path[current_node]:
                    current_node = node

            next_districts = self.get_outgoing_links(current_node)
            for district in next_districts:
                route = shortest_path[current_node] + \
                    self.value(current_node, district)
                if route < shortest_path[district]:
                    shortest_path[district] = route
                    previous_nodes[district] = current_node

            unvisited_nodes.remove(current_node)

        return previous_nodes, shortest_path

    def shortest_distance(self, start_node, target_node):

        previous_nodes, shortest_path = self.dijkstra(start_node)

        path = []
        node = target_node

        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        path.append(start_node)
        shortest = list(reversed(path))

        print("shortest path => " + " -> ".join(shortest))

        return {'path': shortest, 'path_cost': shortest_path[target_node]}
