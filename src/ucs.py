import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return cost, path
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return float("inf"), []
