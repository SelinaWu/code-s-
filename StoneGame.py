def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # rule1: if can take all, do it
        # rule2: if the competitior can take all after, 
        # let it take as less as possible
                        
        for i in range(len(piles)-2,-1,-1):
            piles[i] += piles[i+1]
        print(piles)  
        memo = {}
        
        def dfs(i, M):
            if (i,M) in memo:
                return memo[(i,M)]
            
            # rule1: if can take all, do it
            if i+2*M>=len(piles):                
                memo[(i,M)] = piles[i]
                return piles[i]
            
            memo[(i,M)] = piles[i] - min(dfs(i+x, max(M,x)) for x in range(1,2*M+1))
            return memo[(i,M)]
        
        return dfs(0,1)
