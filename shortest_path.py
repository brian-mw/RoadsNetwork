from lib import RoadNetwork
from graph import Graph

graph = Graph()

graph.add_edge("Mchinji", "Kasungu", 141)
graph.add_edge("Mchinji", "Lilongwe", 109)
graph.add_edge("Lilongwe", "Dowa", 55)
graph.add_edge("Lilongwe", "Dedza", 92)
graph.add_edge("Dowa", "Kasungu", 117)
graph.add_edge("Dowa", "Ntchisi", 38)
graph.add_edge("Dowa", "Salima", 67)
graph.add_edge("Kasungu", "Ntchisi", 66)
graph.add_edge("Ntchisi", "Nkhotakota", 66)
graph.add_edge("Nkhotakota", "Salima", 112)
graph.add_edge("Salima", "Dedza", 96)
graph.add_edge("Dedza", "Ntcheu", 74)
graph.add_edge("Ntcheu", "Ntcheu", 0)


road_network = RoadNetwork(graph.get_nodes(), graph.graph)
print(road_network.shortest_distance(start_node="Mchinji", target_node="Ntcheu"))
