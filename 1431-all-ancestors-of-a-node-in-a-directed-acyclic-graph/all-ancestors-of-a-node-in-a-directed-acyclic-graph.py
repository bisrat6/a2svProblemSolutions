from collections import defaultdict, deque
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        # Build graph
        for u, v in edges:
            graph[u].append(v)

        ans = [[] for _ in range(n)]

        # BFS from each node
        for start in range(n):
            queue = deque([start])
            visited = [False] * n
            visited[start] = True

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        ans[nei].append(start)
                        queue.append(nei)

        return ans