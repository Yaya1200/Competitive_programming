class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0]*len(obstacleGrid[0]) for x in obstacleGrid]
        value = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = value
            else:
                value = 0
                dp[0][i] = value
        value = 1
        for j in range(len(obstacleGrid)):
            if obstacleGrid[j][0] != 1:
                dp[j][0] = value
            else:
                value =  0
                dp[j][0] = value
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0 
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]


        
             

        