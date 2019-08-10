def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        
        
        while nums:
            if len(nums)>=2:
                if nums[0]==nums[1]:
                    nums.pop(0)
                else:
                    break
            else:
                break
        if len(nums)<2:
            return len(nums)
        
        # keep increase/descrease by one param
        # check if curr is large/smaller than pre
        # use the smallest/largest, drop the rest
        
        isIncrease = not (nums[0]>nums[1])
        curr_max_ind = 1
        
        
        while curr_max_ind<len(nums)-1:
            if isIncrease:
                if nums[curr_max_ind]>nums[curr_max_ind+1]:
                    curr_max_ind += 1
                    isIncrease = False
                    
                else:
                    nums.pop(curr_max_ind)
            else:
                if nums[curr_max_ind]<nums[curr_max_ind+1]:
                    curr_max_ind += 1
                    isIncrease = True
                    
                else:
                    nums.pop(curr_max_ind)
        
        return len(nums)
