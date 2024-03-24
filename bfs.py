def bfs(graph, start, goal):
    explored = []

    queue = [[start]]
     
    # If the desired node is 
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph 
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
         
        # Condition to check if the
        # current node is not visited
        if node[0] not in explored:
            neighbours = graph[node[0]]
             
            # Loop to iterate over the 
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                 
                # Condition to check if the 
                # neighbour node is the goal
                if neighbour[0] == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node[0])
 
    # Condition when the nodes 
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return