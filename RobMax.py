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

def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helpRob(root):
            res = [0,0]
            if not root:
                return res
            
            left = helpRob(root.left)
            right = helpRob(root.right)
            # index 0: take current value, not take left/right
            res[0] = left[1]+right[1]+root.val
            # index 1: not take current value, 
            # can choose to take left/right
            res[1] = max(left[0], left[1])+max(right[0],right[1])
            return res
        
        
        return max(helpRob(root))
