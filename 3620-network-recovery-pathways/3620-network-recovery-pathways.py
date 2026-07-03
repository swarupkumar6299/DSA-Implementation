from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        edge_costs = set()

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            edge_costs.add(cost)

        # Topological Sort
        queue = deque(i for i in range(n) if indegree[i] == 0)
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor, _ in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        edge_costs = sorted(edge_costs)

        def is_possible(min_edge_cost):
            INF = float("inf")
            min_cost = [INF] * n
            min_cost[0] = 0

            for node in topo_order:
                if min_cost[node] == INF:
                    continue

                for neighbor, cost in graph[node]:
                    if cost < min_edge_cost:
                        continue

                    # Intermediate nodes must be online
                    if neighbor != n - 1 and not online[neighbor]:
                        continue

                    min_cost[neighbor] = min(
                        min_cost[neighbor],
                        min_cost[node] + cost
                    )

            return min_cost[n - 1] <= k

        left, right = 0, len(edge_costs) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if is_possible(edge_costs[mid]):
                answer = edge_costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return answer