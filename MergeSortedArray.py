def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        used_ind = 0
        main_ind = 0
        used_ind2 = 0
        nums1[-m:] = nums1[:m]
        
        while used_ind2<n:
            if used_ind==m:
                break
            if nums1[n+used_ind]<nums2[used_ind2]:
                nums1[main_ind] = nums1[n+used_ind]
                used_ind += 1    
            else:
                nums1[main_ind] = nums2[used_ind2]
                used_ind2 += 1
            
            main_ind += 1
        
        if used_ind2<n:
            nums1[-len(nums2[used_ind2:]):] = nums2[used_ind2:] 
