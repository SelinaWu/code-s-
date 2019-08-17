    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # sort by first element of list
        points.sort(key=lambda x: x[0])
        # check the current overlap, that is
        arrow = 0
        curr_right = float('-inf')
        
        for ptr in points:
            left, right = ptr
            if left <= curr_right:                
                curr_right = min(curr_right, right)
            else:
                arrow += 1                
                curr_right = right
            
        return arrow
