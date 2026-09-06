class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        player1 = 0
        player2 = 0
        flag = True
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                flag = not flag
            if (i+1) % 6 == 0:
                flag = not flag
            if flag:
                player1 += nums[i]
            else:
                player2 += nums[i]
        return player1 - player2

        