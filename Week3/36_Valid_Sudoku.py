class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_list = []
            for j in range(9):
                if board[i][j] == '.':
                    continue   
                if board[i][j] in row_list:
                    return False
                else:
                    row_list.append(board[i][j])
        
        for i in range(9):
            col_list = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_list:
                    return False
                else:
                    col_list.append(board[j][i])

        
        row = [0, 3, 6]
        col = [0, 3, 6]
        pairs = []
        for i in range(3):
            for j in range(3):
                pair = []
                pair.append(row[i])
                pair.append(col[j])
                pairs.append(pair)


        for i in range(len(pairs)):
            sqr_list = []
            pair = pairs[i]
            for i in range(pair[0], pair[0]+3):
                for j in range(pair[1], pair[1]+3):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] in sqr_list:
                        return False
                    else:
                        sqr_list.append(board[i][j])
            
        
        return True
