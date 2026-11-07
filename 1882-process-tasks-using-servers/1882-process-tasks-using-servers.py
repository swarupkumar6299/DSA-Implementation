class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        free = [(w, i) for i, w in enumerate(servers)]   # (weight, index)
        heapify(free)
        busy = []                                        # (finish_time, weight, index)
        ans = []

        for time, t in enumerate(tasks):
            # servers that are done by now become free again
            while busy and busy[0][0] <= time:
                _, w, i = heappop(busy)
                heappush(free, (w, i))

            if free:
                # take the best free server
                w, i = heappop(free)
                heappush(busy, (time + t, w, i))
            else:
                # nobody is free: wait for the server that finishes first
                end, w, i = heappop(busy)
                heappush(busy, (end + t, w, i))

            ans.append(i)

        return ans
