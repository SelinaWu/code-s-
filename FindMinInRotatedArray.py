    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return self.helpMin(nums)
        left = 0
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)/2
            
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
                
        return nums[right]
    
    def helpMin(self, nums):

        if len(nums)==1:
            return nums[0]
        
        mid = (len(nums)-1)/2
        
        if nums[mid]<nums[-1]:
            return self.helpMin(nums[:mid+1])
        else:
            return self.helpMin(nums[mid+1:])
