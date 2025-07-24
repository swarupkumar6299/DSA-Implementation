from typing import List
from collections import defaultdict

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        subtree_xor = [0] * n
        parent = [-1] * n
        start_time = [0] * n
        end_time = [0] * n
        time = [0]
        
        def dfs(node, par):
            parent[node] = par
            start_time[node] = time[0]
            time[0] += 1
            
            subtree_xor[node] = nums[node]
            for neighbor in graph[node]:
                if neighbor != par:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
            
            end_time[node] = time[0] - 1
        
        dfs(0, -1)
        total_xor = subtree_xor[0]
        
        def is_ancestor(u, v):
            return start_time[u] <= start_time[v] <= end_time[u]
        
        min_score = float('inf')
        
        children = []
        for u, v in edges:
            if parent[u] == v:
                children.append(u)
            else:
                children.append(v)
        
        for i in range(len(children)):
            for j in range(i + 1, len(children)):
                child1, child2 = children[i], children[j]
                
                xor1 = subtree_xor[child1]
                xor2 = subtree_xor[child2]
                
                if is_ancestor(child1, child2):
                    xor1 = subtree_xor[child1] ^ xor2
                    xor3 = total_xor ^ subtree_xor[child1]
                elif is_ancestor(child2, child1):
                    xor2 = subtree_xor[child2] ^ xor1
                    xor3 = total_xor ^ subtree_xor[child2]
                else:
                    xor3 = total_xor ^ xor1 ^ xor2
                
                components = [xor1, xor2, xor3]
                score = max(components) - min(components)
                min_score = min(min_score, score)
                
                if min_score == 0:
                    return 0
        
        return min_score