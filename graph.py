# function called build_graph() is created and returns 'graph' obect that can be searched

# importing  dictionaries
from collections import defaultdict

# Initializeing the graph


def build_graph():
    edges = [("A", "B", 3), ("A", "C", 4), ("A", "E", 5), ("B", "A", 3), ("B", "D", 1), ("B", "E", 2), ("C", "A", 4), ("C", "F", 2), ("C", "G", 2),
             ("D", "B", 1), ("D", "E", 3), ("E", "A", 5), ("E", "B", 2), ("E", "D", 3), ("E", "F", 3), ("F", "C", 2), ("F", "E", 3), ("G", "C", 2)]

    # storing the "edges" lsit in a dictionary which is stored as 'graph'
    graph = defaultdict(list)

# Iterate over the edges. WE CAN DELETE THE FOR-LOOP WHEN WE HAVE THE BFS, AS THIS
  # WAS HERE JUST TO MAKE SURE THE GRAPH WAS BEING CREATED CORRECTLY

    for (source, dest, weight) in edges:
        graph[source].append((dest, weight))

        # Print the edge & its weight
        print(f"{source} <--> {dest} (weight: {weight})")

    return graph
