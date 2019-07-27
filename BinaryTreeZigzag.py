    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        
        # left->right, right->left
        level = 0
        queue = [(level, root)]
        one_floor = []
        result = []
        while queue:
            curr_level, curr_node = queue.pop(0)
            
            if curr_level>level:
                if level%2==0:
                    result.append(one_floor)
                else:
                    result.append(one_floor[::-1])
                level = curr_level
                one_floor = []

            one_floor.append(curr_node.val)
            if curr_node.left:
                queue.append((curr_level+1, curr_node.left))
            if curr_node.right:
                queue.append((curr_level+1, curr_node.right))
        
        if one_floor:
            if level%2==0:
                result.append(one_floor)
            else:
                result.append(one_floor[::-1])

        return result
