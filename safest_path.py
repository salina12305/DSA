import math
import heapq

# Graph with safety probabilities
graph = {
    "KTM": {"JA": 0.9, "JB": 0.8},
    "JA": {"PH": 0.95, "BS": 0.7},
    "JB": {"JA": 0.6, "BS": 0.9},
    "PH": {"BS": 0.85},
    "BS": {}
}
def safest_path(graph, source):
    dist = {node: float("inf") for node in graph}
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        for v, prob in graph[u].items():
            weight = -math.log(prob)
            if dist[v] > current_dist + weight:
                dist[v] = current_dist + weight
                heapq.heappush(pq, (dist[v], v))
    return dist
# ✅ CALL the function (this was missing)
result = safest_path(graph, "KTM")
print("Safest path probabilities from KTM:")
for node, value in result.items():
    if value < float("inf"):
        print(node, ":", round(math.exp(-value), 4))
