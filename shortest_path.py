from lib import RoadNetwork

nodes = ["Mchinji", "Kasungu", "Lilongwe", "Ntchisi",
         "Dowa", "Dedza", "Ntcheu", "Salima", "Nkhotakota"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Mchinji"]["Kasungu"] = 141
init_graph["Mchinji"]["Lilongwe"] = 109
init_graph["Lilongwe"]["Dowa"] = 55
init_graph["Lilongwe"]["Dedza"] = 92
init_graph["Dowa"]["Kasungu"] = 117
init_graph["Dowa"]["Ntchisi"] = 38
init_graph["Dowa"]["Salima"] = 67
init_graph["Kasungu"]["Ntchisi"] = 66
init_graph["Ntchisi"]["Nkhotakota"] = 66
init_graph["Nkhotakota"]["Salima"] = 112
init_graph["Salima"]["Dedza"] = 96
init_graph["Dedza"]["Ntcheu"] = 74

graph = RoadNetwork(nodes, init_graph)
print(graph.shortest_distance(start_node="Lilongwe", target_node="Nkhotakota"))
