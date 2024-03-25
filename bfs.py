import heapq

def bfs(graph, start, goal):
    explored = set()
    queue = [(0, [start])]  # (priority, path)

    if start == goal:
        print("Same Node")
        return

    while queue:
        priority, path = heapq.heappop(queue)
        node = path[-1]

        if node not in explored:
            explored.add(node)

            if node == goal:
                print("Shortest path =", *path)
                return

            for neighbour, edge_cost in graph[node]:
                if neighbour not in explored:
                    new_priority = priority + edge_cost
                    new_path = list(path)
                    new_path.append(neighbour)
                    heapq.heappush(queue, (new_priority, new_path))

    print("So sorry, but a connecting path doesn't exist :(")
    return