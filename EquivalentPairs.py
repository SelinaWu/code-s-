def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        res = dict()
        total = 0
        
        for pair in dominoes:
            pair.sort()
            
            pair = tuple(pair)
            if pair in res:
                temp0 = res[pair]
                total += temp0
                res[pair] = temp0+1
                
            else:
                res[pair] = 1
                
        return total
