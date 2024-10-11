class Solution:
    # O(nlogn) time | O(n) space
    # n = # of friends
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        sorted_times = []
        for i in range(n):
            arrival, departure = times[i]
            sorted_times.append((arrival, departure, i))

        new_chair = 0
        sorted_times.sort() # sorted list of (arrival, departure, friend)
        chairs_in_use = []  # min heap of (time when free, chair #)
        chairs_free = []    # min heap of (chairs #)

        for arrival, departure, friend in sorted_times:
            while chairs_in_use and chairs_in_use[0][0] <= arrival:
                _, freed_chair = heappop(chairs_in_use)
                heappush(chairs_free, freed_chair)

            assigned_chair = -1
            if chairs_free:
                assigned_chair = heappop(chairs_free)
            else:
                assigned_chair = new_chair
                new_chair += 1

            if friend == targetFriend:
                return assigned_chair
            heappush(chairs_in_use, (departure, assigned_chair))

        return -1