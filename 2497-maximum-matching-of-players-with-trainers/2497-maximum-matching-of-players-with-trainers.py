class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        length_t = len(trainers)
        length_p = len(players)
        output = 0
        count = 0
        while count < length_t and output < length_p:
            if trainers[count] >= players[output]:
                output += 1
                count +=1
            else:
                count += 1
        return output