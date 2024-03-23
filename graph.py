#importing  dictionaries
from collections import defaultdict

#Initializeing the graph

def build_graph():
    edges = [
         ["A", "B", 3], ["A", "E", 1], 
        ["A", "C", 4], ["B", "D", 1],
        ["B", "E", 2], ["C", "F", 1],
        ["C", "G", 1], ["D", "E", 3]
    ]

    graph = defaultdict(list)

  # Iterate over the edges. WE CAN DELETE THE FOR-LOOP WHEN WE HAVE THE BFS, AS THIS
  #WAS HERE JUST TO MAKE SURE THE GRAPH WAS BEING CREATED CORRECTLY 
    for edge in edges:
        source, dest, weight = edge

        # Add the edge to the graph with the weight as the second element
        graph[source].append((dest, weight))

        # Print the edge
        print(f"{source} <--> {dest} (weight: {weight})")

    return graph

build_graph() # Calling the function to initialize & Output Graph edges & Weights