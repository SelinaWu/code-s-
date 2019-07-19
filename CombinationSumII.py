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
        if temp in result: 
            return
        result.append(temp)
        return 

    for i in range(curr_ind, len(tank)):
        if tank[i]>k:
            continue

        self.helpComb(tank, k-tank[i], result, temp+[tank[i]], i+1)
