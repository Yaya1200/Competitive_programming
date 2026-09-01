class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {0: 1}

        for i in nums:

            newdp = {}

            for total, value in dp.items():

                newvalue = i + total

                if newvalue in newdp:
                    newdp[newvalue] += value
                else:
                    newdp[newvalue] = value

                newvalue = total - i

                if newvalue in newdp:
                    newdp[newvalue] += value
                else:
                    newdp[newvalue] = value

            dp = newdp

        return dp.get(target, 0)