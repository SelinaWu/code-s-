def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # to select (k+3), then must skip (k+2)
        # consider (k+1) or (k) 
        length = len(nums)
        if length==0:
            return 0
        if length<3:
            return max(nums)
        
        nums[2] += nums[0]
        
        for i in range(3, length):
            nums[i] += max(nums[i-2], nums[i-3])
            
        return max(nums[-1], max(nums[-2], nums[-3]))
