class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for r in range(row):
            for c in range(col):
                # row wise
                seen_row=set()
                for ci in range(col):
                    if board[r][ci]!='.':
                        if board[r][ci] in seen_row:
                            return False
                        seen_row.add(board[r][ci])
                ## col wise
                seen_col=set()
                for ri in range(row):
                    if board[ri][c]!='.':
                        if board[ri][c] in seen_col:
                            return False
                        seen_col.add(board[ri][c])
                ## 3*3 grid wise check
                seen_box=set()
                s_row=(r//3)*3
                s_col=(c//3)*3
                for rb in range(3):
                    for cb in range(3):
                        val=board[rb+s_row][cb+s_col]
                        if val!='.':
                            if val in seen_box:
                                return False
                            seen_box.add(val)
        return True
            