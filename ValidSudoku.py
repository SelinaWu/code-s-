def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
         
        in_row = dict()
        in_col = dict()
        sub_box = dict()
       
        
        for i in range(9):
            in_row = [0]*9
            for j in range(9):
                val = board[i][j]
                if val=='.':
                    continue
                    
                val = int(val)-1
                
                if in_row[val]==1:
                    return False
                else:
                    in_row[val]=1
                
                if j in in_col.keys():
                    temp_ls = in_col[j]
                    if temp_ls[val]==1:
                        return False
                    else:
                        in_col[j][val]=1
                else:
                    in_col[j] = [0]*9
                    in_col[j][val]=1
                    
                grid_ind = int(i/3*10+j/3)
                if grid_ind in sub_box.keys():
                    temp_ls = sub_box[grid_ind]
                    if temp_ls[val]==1:
                        return False
                    else:
                        sub_box[grid_ind][val]=1
                else:
                    sub_box[grid_ind] = [0]*9
                    sub_box[grid_ind][val]=1
                    
        return True
