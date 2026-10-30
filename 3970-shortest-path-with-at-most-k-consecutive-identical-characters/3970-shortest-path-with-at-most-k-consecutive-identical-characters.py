class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        
        # Dijkstra's algorithm with state (node, last_char, consecutive_count)
        # Store minimum distance for each state
        dist = {}
        pq = []
        
        # Initial state: at node 0 with its label, count = 1
        start_char = labels[0]
        state = (0, start_char, 1)
        dist[state] = 0
        heapq.heappush(pq, (0, 0, start_char, 1))
        
        while pq:
            weight, node, last_char, count = heapq.heappop(pq)
            
            # Skip outdated entries
            if weight != dist.get((node, last_char, count), float('inf')):
                continue
            
            # Found shortest path to destination
            if node == n - 1:
                return weight
            
            # Explore neighbors
            for neighbor, edge_weight in graph[node]:
                next_char = labels[neighbor]
                
                # Update consecutive count based on label match
                if next_char == last_char:
                    new_count = count + 1
                    if new_count > k:
                        continue  # Invalid path
                else:
                    new_count = 1
                
                new_state = (neighbor, next_char, new_count)
                new_weight = weight + edge_weight
                
                # Update if we found a better path to this state
                if new_weight < dist.get(new_state, float('inf')):
                    dist[new_state] = new_weight
                    heapq.heappush(pq, (new_weight, neighbor, next_char, new_count))
        
        return -1