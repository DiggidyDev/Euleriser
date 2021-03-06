from graph import Graph

graph = Graph(4)  # INITIALISE THE GRAPH SIZE HERE
gui = graph.init_gui()

graph.add_path(1, 2)
graph.add_path(1, 4)
graph.add_path(2, 4)
graph.add_path(3, 4)

print(graph.get_node(4).get_all_distances()) # Returns dictionary with all node identifiers and their respective distances
print(graph.get_node(4).distance_from(2)) # Returns distance between two nodes
print(graph.get_node(4).distance_from()) # Returns minimum distance

graph.analysis()

graph.search(graph.get_node(3))  # EDIT THE STARTING NODE HERE!

print(graph)
