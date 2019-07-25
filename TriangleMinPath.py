def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        
        memo_upper = [float('inf'), triangle[0][0], float('inf')]
        memo_down = [x for x in triangle[1]]
        
        for k in range(1, len(triangle)):
            for j in range(len(memo_down)):
                memo_down[j] += min(memo_upper[j], memo_upper[j+1])
                  
            if k+1!=len(triangle):
                memo_upper = [float('inf')]+memo_down+[float('inf')]
                memo_down = [x for x in triangle[k+1]]
            
        return min(memo_down)
