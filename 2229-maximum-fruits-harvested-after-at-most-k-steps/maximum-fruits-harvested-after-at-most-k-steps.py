class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
    
        fruitMap = defaultdict(int)
        
        for position, amount in fruits:
            fruitMap[position] = amount
        
        
        if k == 0:
            return fruitMap[startPos]
        
        totalLeft = 0 
        totalRight = 0 
        inBetween = 0 
        dp = dict()
        
        for i in range(startPos,startPos-k-1, -1):
            totalLeft += fruitMap[i]
            dp[i] = totalLeft
            
        for i in range(startPos,startPos+k+1):
            totalRight += fruitMap[i]
            dp[i] = totalRight
            
        
        leftSteps = 1
        rightSteps = k-2
        
        while rightSteps > 0:
            currAmount = 0
            
            currAmount += dp[startPos-leftSteps]
            currAmount += dp[startPos+rightSteps]
            
            
            inBetween = max(inBetween, currAmount-fruitMap[startPos])
            
            leftSteps += 1
            rightSteps -= 2
        
        
        leftSteps = k-2
        rightSteps = 1
        
        while leftSteps > 0:
            currAmount = 0
            
            currAmount += dp[startPos-leftSteps]
            currAmount += dp[startPos+rightSteps]
            
            inBetween = max(inBetween, currAmount-fruitMap[startPos])
            
            leftSteps -= 2
            rightSteps += 1
        
            
        return max(totalLeft, totalRight, inBetween)