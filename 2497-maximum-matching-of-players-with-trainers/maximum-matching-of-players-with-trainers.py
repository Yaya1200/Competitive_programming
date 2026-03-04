class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players)
        trainers = sorted(trainers)
        i = 0
        j = 0
        count = 0
        while(i < len(players) and j < len(trainers)):
            if players[i] <= trainers[j]:
                j+= 1
                i+= 1
                count += 1
            else:
                j+=1
        return count
        