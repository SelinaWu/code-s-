def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        
        self.helpComb(candidates, target,result,[], 0)
        return result
    
def helpComb(self, tank, k, result, temp, curr_ind):
        if k<0:
            return 
        if k==0:
            
            result.append(temp)
            return 
        buff = 0
        for i in range(curr_ind, len(tank)):
            if tank[i]>k:
                break
            if tank[i]==buff:
                continue
            buff = tank[i]
            self.helpComb(tank, k-buff, result, temp+[buff], i+1)
