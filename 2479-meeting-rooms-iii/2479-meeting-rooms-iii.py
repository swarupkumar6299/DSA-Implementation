from dataclasses import dataclass

@dataclass(order=True)
class Room:
    end_time: int
    room_num: int
    counter: int

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms: list[Room] = [Room(0, room_num, 0) for room_num in range(n)]
        used: list[Room] = []

        heapq.heapify(rooms)
        meetings.sort()

        for start, end in meetings:
            while used and used[0].end_time <= start:
                room = heapq.heappop(used)
                room.end_time = 0 # reset
                heapq.heappush(rooms, room)
                
            # we try to get an available room if possible. If not, we pick a used room
            # and adjust our end time according to the fact that the meeting will occur
            # in the future.
            room = heapq.heappop(rooms) if rooms else heapq.heappop(used)
            room.end_time = end if room.end_time == 0 else room.end_time + (end - start)
            room.counter += 1
            heapq.heappush(used, room)
        
        while used:
            heapq.heappush(rooms, heapq.heappop(used))
        return max(rooms, key=lambda x: (x.counter, -x.room_num)).room_num