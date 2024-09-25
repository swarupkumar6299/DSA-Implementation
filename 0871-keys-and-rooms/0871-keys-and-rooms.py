class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        KeyList = [0]
        KeySet = {0}
        solved = False
        while len(KeyList) != 0 and not solved:
            Keys = rooms[KeyList.pop()]
            for Key in Keys:
                if not Key in (KeySet):
                    KeyList.append(Key)
                    KeySet.add(Key)
            if len(KeySet) == len(rooms):
                solved = True
        return solved
        